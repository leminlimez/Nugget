from __future__ import annotations

from enum import Enum
import asyncio
import functools
import os
import posixpath
import queue
import re
import shutil
import socket
import sqlite3
import subprocess
import sys
import tempfile
import threading
import time
import uuid as uuid_mod
import atexit
from http.server import HTTPServer, SimpleHTTPRequestHandler
from typing import Callable, Optional

from .restore import FileToRestore
from exceptions.nugget_exception import NuggetException
from gui.apply_worker import get_sudo_pwd, get_sudo_complete
from controllers.files_handler import get_bundle_files

from pymobiledevice3.lockdown import LockdownClient
from pymobiledevice3.services.afc import AfcService
from pymobiledevice3.services.amfi import AmfiService
from pymobiledevice3.remote.remote_service_discovery import RemoteServiceDiscoveryService
from pymobiledevice3.services.dvt.dvt_secure_socket_proxy import DvtSecureSocketProxyService
from pymobiledevice3.services.dvt.instruments.process_control import ProcessControl
from pymobiledevice3.services.os_trace import OsTraceService


class BookRestoreFileTransferMethod(Enum):
    LocalHost = 0
    OnDevice = 1


# Tunables (chosen to be conservative / less flaky)
TUNNEL_START_TIMEOUT_S = 90
RSD_CONNECT_RETRIES = 10
RSD_CONNECT_RETRY_SLEEP_S = 1.5

UUID_DISCOVERY_TIMEOUT_S = 240
ITUNESSTORED_WAIT_TIMEOUT_S = 180
OVERWRITE_WAIT_TIMEOUT_S_LOCALHOST = 30
OVERWRITE_WAIT_TIMEOUT_S_ONDEVICE = 120


def _safe_call(cb: Callable, *args, **kwargs):
    try:
        return cb(*args, **kwargs)
    except Exception:
        return None


def _run_coro_blocking(coro):
    """
    Run a coroutine from both sync and already-async contexts safely.

    - If there's no running loop in this thread: asyncio.run(coro)
    - If there is: run in a dedicated thread with its own loop.
    """
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(coro)

    result_q: "queue.Queue[tuple[bool, object]]" = queue.Queue()

    def _runner():
        try:
            result_q.put((True, asyncio.run(coro)))
        except BaseException as e:
            result_q.put((False, e))

    t = threading.Thread(target=_runner, daemon=True)
    t.start()
    ok, payload = result_q.get()
    if not ok:
        raise payload
    return payload


def get_lan_ip() -> str:
    """
    Best-effort LAN IPv4 detection. Falls back to loopback if offline / blocked.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't send packets; just asks OS what source IP would be used.
        s.connect(("1.1.1.1", 80))
        ip = s.getsockname()[0]
        if ip:
            return ip
    except OSError:
        pass
    finally:
        try:
            s.close()
        except Exception:
            pass

    # Fallbacks
    try:
        ip = socket.gethostbyname(socket.gethostname())
        if ip and not ip.startswith("127."):
            return ip
    except OSError:
        pass

    return "127.0.0.1"


class _QuietHTTPRequestHandler(SimpleHTTPRequestHandler):
    # SimpleHTTPRequestHandler is noisy; Nugget doesn't need request logs.
    def log_message(self, format, *args):  # noqa: N802
        return


class _TempHTTPServer:
    """
    A tiny HTTP server (threaded) used to serve BLDatabaseManager sqlite files to the device.
    """
    def __init__(self, directory: str, bind_host: str = "0.0.0.0", port: int = 0):
        self.directory = directory
        self.bind_host = bind_host
        self.port = port
        self.httpd: Optional[HTTPServer] = None
        self.thread: Optional[threading.Thread] = None

    def start(self) -> tuple[str, int]:
        handler = functools.partial(_QuietHTTPRequestHandler, directory=self.directory)
        self.httpd = HTTPServer((self.bind_host, self.port), handler)
        self.port = self.httpd.server_port
        ip = get_lan_ip()
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()
        return ip, self.port

    def stop(self):
        try:
            if self.httpd:
                self.httpd.shutdown()
                self.httpd.server_close()
        except Exception:
            pass
        try:
            if self.thread:
                self.thread.join(timeout=2)
        except Exception:
            pass


def _terminate_process(proc: subprocess.Popen):
    try:
        proc.terminate()
    except Exception:
        pass
    try:
        proc.wait(timeout=2)
    except Exception:
        try:
            proc.kill()
        except Exception:
            pass


def _parse_tunnel_output(lines: list[str]) -> Optional[tuple[str, int]]:
    """
    Parse pymobiledevice3 tunnel output in multiple known formats.
    Returns (address, port) if found.
    """
    addr = None
    port = None

    # Common "script-mode" output in Nugget: "<addr> <port>"
    direct_re = re.compile(r"^(?P<addr>\S+)\s+(?P<port>\d+)\s*$")

    # Non script-mode output often includes "RSD Address:" and "RSD Port:"
    rsd_addr_re = re.compile(r"RSD\s+Address:\s*(?P<addr>\S+)")
    rsd_port_re = re.compile(r"RSD\s+Port:\s*(?P<port>\d+)")
    rsd_flag_re = re.compile(r"--rsd\s+(?P<addr>\S+)\s+(?P<port>\d+)")

    for raw in lines:
        line = (raw or "").strip()
        if not line:
            continue

        m = direct_re.match(line)
        if m:
            return m.group("addr"), int(m.group("port"))

        m = rsd_flag_re.search(line)
        if m:
            return m.group("addr"), int(m.group("port"))

        m = rsd_addr_re.search(line)
        if m:
            addr = m.group("addr").strip() or addr

        m = rsd_port_re.search(line)
        if m:
            try:
                port = int(m.group("port"))
            except Exception:
                pass

        if addr and port:
            return addr, port

    return None


async def create_tunnel(udid: str, progress_callback: Callable[[str], None] = lambda x: None):
    """
    Starts a pymobiledevice3 lockdown tunnel and returns {"address": ..., "port": ...}.

    Reliability improvements vs the original Nugget script:
    - Avoids shell=True and sudo password piping hacks
    - Uses executor to avoid blocking the event loop while reading stdout
    - More robust parsing + timeouts
    """
    base_args = [
        sys.executable,
        "-m",
        "pymobiledevice3",
        "lockdown",
        "start-tunnel",
        "--script-mode",
        "--udid",
        udid,
    ]

    stdin = None
    pwd = None
    if os.name != "nt":
        if hasattr(os, "geteuid") and os.geteuid() != 0:
            progress_callback("sudo_pwd")
            while not get_sudo_complete():
                await asyncio.sleep(0.5)
            pwd = get_sudo_pwd()
            if not pwd:
                raise NuggetException("No administrator permission")
            # sudo reads password from stdin when -S is set
            base_args = ["sudo", "-S"] + base_args
            stdin = subprocess.PIPE

    try:
        tunnel_process = subprocess.Popen(
            base_args,
            stdin=stdin,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
        )
    except FileNotFoundError as e:
        raise NuggetException("Failed to start tunnel process.", detailed_text=repr(e))

    atexit.register(_terminate_process, tunnel_process)

    if pwd and tunnel_process.stdin:
        try:
            tunnel_process.stdin.write(pwd + "\n")
            tunnel_process.stdin.flush()
        except Exception:
            pass
        finally:
            # best-effort scrub
            pwd = None

    start = time.time()
    recent_lines: list[str] = []
    loop = asyncio.get_running_loop()

    while True:
        if time.time() - start > TUNNEL_START_TIMEOUT_S:
            _terminate_process(tunnel_process)
            err = ""
            try:
                err = (tunnel_process.stderr.read() if tunnel_process.stderr else "") or ""
            except Exception:
                pass
            raise NuggetException(
                "Timed out starting tunnel. Make sure the device is connected and trusted.",
                detailed_text=err.strip() or None,
            )

        # read one stdout line without blocking loop
        line = await loop.run_in_executor(None, tunnel_process.stdout.readline)  # type: ignore[arg-type]
        if line:
            recent_lines.append(line)
            # cap buffer
            if len(recent_lines) > 50:
                recent_lines = recent_lines[-50:]

            parsed = _parse_tunnel_output(recent_lines[-10:])
            if parsed:
                address, port = parsed
                print(f"Successfully created tunnel: {address} {port}")
                return {"address": address, "port": port}

        else:
            # No output. Check for exit.
            if tunnel_process.poll() is not None:
                try:
                    error = tunnel_process.stderr.read()
                except Exception:
                    error = ""
                error = (error or "").strip()
                if error:
                    low = error.lower()
                    if "connected" in low or "no device" in low:
                        raise NuggetException("Device not connected.", detailed_text=error)
                    if "admin" in low or "permission" in low or "sudo" in low:
                        raise NuggetException("Admin privileges required.", detailed_text=error)
                    raise NuggetException("Tunnel Error.", detailed_text=error)
                raise NuggetException("Tunnel process ended without returning connection details.")


async def create_connection_context(
    files: list[FileToRestore],
    service_provider: LockdownClient,
    current_device_uuid_callback: Callable[..., Optional[str]] = lambda *args, **kwargs: None,
    progress_callback: Callable[[str], None] = lambda x: None,
    transfer_mode: BookRestoreFileTransferMethod = BookRestoreFileTransferMethod.LocalHost,
):
    available_address = await create_tunnel(service_provider.udid, progress_callback)
    if not available_address:
        raise NuggetException("An error occurred getting tunnel address...")

    addr = available_address["address"]
    port = available_address["port"]

    last_err: Optional[Exception] = None
    for i in range(RSD_CONNECT_RETRIES):
        try:
            async with RemoteServiceDiscoveryService((addr, port)) as rsd:
                loop = asyncio.get_running_loop()

                def run_blocking():
                    with DvtSecureSocketProxyService(rsd) as dvt:
                        apply_bookrestore_files(
                            files,
                            rsd,
                            dvt,
                            current_device_uuid_callback,
                            progress_callback,
                            transfer_mode,
                        )

                await loop.run_in_executor(None, run_blocking)
                return
        except OSError as e:
            last_err = e
            if isinstance(e, PermissionError) or getattr(e, "errno", None) == 13:
                raise
            print(f"Connection attempt {i + 1}/{RSD_CONNECT_RETRIES} failed: {e}")
            await asyncio.sleep(RSD_CONNECT_RETRY_SLEEP_S)

    if last_err:
        raise last_err


def remove_db_files(db_path: str):
    for ext in ["", "-shm", "-wal"]:
        fpath = db_path + ext
        if os.path.exists(fpath):
            try:
                os.remove(fpath)
            except Exception:
                pass


def _netsh_add_firewall_rule(port: int) -> Optional[str]:
    """
    Best-effort Windows firewall allow rule (inbound). Returns rule name if created.
    """
    if os.name != "nt":
        return None
    rule_name = f"Nugget_Temp_{port}"
    try:
        subprocess.run(
            [
                "netsh",
                "advfirewall",
                "firewall",
                "add",
                "rule",
                f"name={rule_name}",
                "dir=in",
                "action=allow",
                "protocol=TCP",
                f"localport={port}",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        return rule_name
    except Exception:
        return None


def _netsh_delete_firewall_rule(rule_name: str):
    if os.name != "nt" or not rule_name:
        return
    try:
        subprocess.run(
            ["netsh", "advfirewall", "firewall", "delete", "rule", f"name={rule_name}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except Exception:
        pass


def _kill_if_running(pc: ProcessControl, pid: Optional[int]):
    if not pid:
        return
    try:
        pc.kill(pid)
    except Exception:
        pass


def _signal_if_running(pc: ProcessControl, pid: Optional[int], sig: int):
    if not pid:
        return
    try:
        pc.signal(pid, sig)
    except Exception:
        pass


def _launch_app(pc: ProcessControl, bundle_id: str):
    try:
        pc.launch(bundle_id)
    except Exception as e:
        raise NuggetException(f"Error launching {bundle_id}", detailed_text=repr(e))


def _get_ios_version(lockdown_client: LockdownClient) -> str:
    """
    Best-effort iOS version lookup for populating metadata fields.
    """
    for attr in ("product_version", "ProductVersion", "productVersion"):
        try:
            v = getattr(lockdown_client, attr)
            if isinstance(v, str) and v:
                return v
        except Exception:
            pass
    try:
        v = lockdown_client.get_value(None, "ProductVersion")
        if isinstance(v, str) and v:
            return v
    except Exception:
        pass
    return ""


def _get_pid_by_name(lockdown_client: LockdownClient, name: str) -> Optional[int]:
    try:
        procs = OsTraceService(lockdown=lockdown_client).get_pid_list().get("Payload") or {}
    except Exception:
        return None
    try:
        return next((pid for pid, p in procs.items() if (p or {}).get("ProcessName") == name), None)
    except Exception:
        return None


def _wait_for_syslog(
    lockdown_client: LockdownClient,
    predicate: Callable[[object], bool],
    timeout_s: int,
):
    """
    Best-effort syslog wait. Note: if syslog stream itself blocks without yielding,
    the timeout may not be exact (this mirrors upstream behavior).
    """
    deadline = time.time() + timeout_s
    for entry in OsTraceService(lockdown=lockdown_client).syslog():
        if time.time() > deadline:
            return None
        try:
            if predicate(entry):
                return entry
        except Exception:
            continue
    return None


def apply_bookrestore_files(
    files: list[FileToRestore],
    lockdown_client: LockdownClient,
    dvt: DvtSecureSocketProxyService,
    current_device_uuid_callback: Callable[..., Optional[str]] = lambda *args, **kwargs: None,
    progress_callback: Callable[[str], None] = lambda x: None,
    transfer_mode: BookRestoreFileTransferMethod = BookRestoreFileTransferMethod.LocalHost,
):
    """
    Apply BookRestore payload with reliability tweaks:
    - safer cleanup (HTTP server, firewall rules, temp files)
    - guards around None PIDs / callbacks
    - less brittle syslog parsing for the itunesstored stage
    - fixes a common bug: do NOT shadow the uuid module (container_uuid instead)
    """
    br_files = get_bundle_files("files/bookrestore")
    if not os.path.exists(br_files):
        br_files = get_bundle_files("")
    br_files = os.path.abspath(br_files)

    http_server = None
    fw_rule = None
    ip = None
    port = None

    if transfer_mode == BookRestoreFileTransferMethod.LocalHost:
        http_server = _TempHTTPServer(directory=br_files)
        ip, port = http_server.start()
        print(f"Hosting temporary http server on: http://{ip}:{port}/")
        fw_rule = _netsh_add_firewall_rule(port)

    afc = AfcService(lockdown=lockdown_client)
    pc = ProcessControl(dvt)

    try:
        # Get Container UUID
        container_uuid = (_safe_call(current_device_uuid_callback) or "")
        container_uuid = container_uuid.strip() if isinstance(container_uuid, str) else ""
        if len(container_uuid) < 10:
            # Ensure Books is launched, then watch syslog for the BLDownloads path.
            try:
                _launch_app(pc, "com.apple.iBooks")
            except NuggetException:
                pass

            progress_callback("Please open Books app and download a book to continue.")

            def _uuid_pred(entry):
                fname = posixpath.basename(getattr(entry, "filename", "") or "")
                msg = getattr(entry, "message", "") or ""
                return fname == "bookassetd" and "/Documents/BLDownloads/" in msg

            hit = _wait_for_syslog(lockdown_client, _uuid_pred, UUID_DISCOVERY_TIMEOUT_S)
            if not hit:
                raise NuggetException(
                    "Timed out waiting to discover the Books container UUID. Try downloading any book in Books and retry."
                )

            msg = getattr(hit, "message", "") or ""
            try:
                container_uuid = msg.split("/var/containers/Shared/SystemGroup/")[1].split("/Documents/BLDownloads")[0]
            except Exception:
                raise NuggetException("Failed to parse Books container UUID from syslog.", detailed_text=msg)

            _safe_call(current_device_uuid_callback, container_uuid)

        sqlite_path = os.path.join(br_files, "downloads.28.sqlitedb")
        dl_manager_src = os.path.join(br_files, "BLDatabaseManager.sqlite")
        file_attr_path = os.path.join(br_files, "zfileattributes.plist")

        if not os.path.exists(sqlite_path):
            raise NuggetException("Missing template downloads DB.", detailed_text=sqlite_path)
        if not os.path.exists(dl_manager_src):
            raise NuggetException("Missing BLDatabaseManager.sqlite template.", detailed_text=dl_manager_src)
        if transfer_mode == BookRestoreFileTransferMethod.LocalHost and not os.path.exists(file_attr_path):
            raise NuggetException("Missing zfileattributes.plist.", detailed_text=file_attr_path)

        bldb_local_prefix = f"/private/var/containers/Shared/SystemGroup/{container_uuid}/Documents/BLDatabaseManager/BLDatabaseManager.sqlite"

        # Use a unique temp folder per run to avoid collisions.
        run_tmp_dir = tempfile.mkdtemp(prefix=f"nugget_bookrestore_{container_uuid}_")
        temp_db_path = os.path.join(run_tmp_dir, "downloads.28.sqlitedb")

        # Must live inside served directory for LocalHost mode (http server path)
        temp_dl_manager = os.path.join(br_files, "tmp.BLDatabaseManager.sqlite")
        remove_db_files(temp_dl_manager)

        expected_overwrites = 0

        try:
            shutil.copyfile(sqlite_path, temp_db_path)

            # Patch downloads.28.sqlitedb
            with sqlite3.connect(temp_db_path) as conn:
                cur = conn.cursor()
                cur.execute(
                    """
                    UPDATE asset
                    SET local_path = CASE
                        WHEN local_path LIKE '%/BLDatabaseManager.sqlite' THEN ?
                        WHEN local_path LIKE '%/BLDatabaseManager.sqlite-shm' THEN ?
                        WHEN local_path LIKE '%/BLDatabaseManager.sqlite-wal' THEN ?
                        ELSE local_path
                    END
                    WHERE local_path LIKE '/private/var/containers/Shared/SystemGroup/%/Documents/BLDatabaseManager/BLDatabaseManager.sqlite%'
                    """,
                    (bldb_local_prefix, f"{bldb_local_prefix}-shm", f"{bldb_local_prefix}-wal"),
                )

                if transfer_mode == BookRestoreFileTransferMethod.LocalHost:
                    bldb_server_prefix = f"http://{ip}:{port}/tmp.BLDatabaseManager.sqlite"
                else:
                    # On-device mode uses upstream-hosted sqlite. Keep Nugget logic.
                    bldb_server_prefix = (
                        "https://github.com/leminlimez/Nugget/raw/refs/heads/main/.on_device_remote_files/BLDatabaseManager-mga"
                    )
                    if any(getattr(f, "restore_path", "").endswith("com.apple.iokit.IOMobileGraphicsFamily.plist") for f in files):
                        bldb_server_prefix += "+iokit"
                    bldb_server_prefix += ".sqlite"

                cur.execute(
                    """
                    UPDATE asset
                    SET url = CASE
                        WHEN url LIKE '%/BLDatabaseManager.sqlite' THEN ?
                        WHEN url LIKE '%/BLDatabaseManager.sqlite-shm' THEN ?
                        WHEN url LIKE '%/BLDatabaseManager.sqlite-wal' THEN ?
                        ELSE url
                    END
                    WHERE url LIKE '%/BLDatabaseManager.sqlite%'
                    """,
                    (bldb_server_prefix, f"{bldb_server_prefix}-shm", f"{bldb_server_prefix}-wal"),
                )
                conn.commit()

            # Pause/kill some processes to reduce races.
            pid_bookassetd = _get_pid_by_name(lockdown_client, "bookassetd")
            pid_books = _get_pid_by_name(lockdown_client, "Books")
            if pid_bookassetd:
                _signal_if_running(pc, pid_bookassetd, 19)
            if pid_books:
                _kill_if_running(pc, pid_books)

            progress_callback("Uploading files...")

            # Update the BLDatabaseManager download db (LocalHost mode only).
            z_id = 0
            if transfer_mode == BookRestoreFileTransferMethod.LocalHost:
                shutil.copyfile(dl_manager_src, temp_dl_manager)
                with sqlite3.connect(temp_dl_manager) as dl_conn:
                    dl_cur = dl_conn.cursor()
                    dl_cur.execute("DELETE FROM ZBLDOWNLOADINFO")

                    with open(file_attr_path, "rb") as attr_file:
                        attr_data = attr_file.read()

                    # Ensure NuggetPayload exists.
                    nugget_media_folder = "NuggetPayload"
                    try:
                        if not afc.exists(nugget_media_folder):
                            afc.makedirs(nugget_media_folder)
                    except Exception:
                        pass

                    insert_sql = """
                    INSERT INTO ZBLDOWNLOADINFO (
                        Z_PK, Z_ENT, Z_OPT, ZACCOUNTIDENTIFIER, ZCLEANUPPENDING, ZFAMILYACCOUNTIDENTIFIER,
                        ZISAUTOMATICDOWNLOAD, ZISLOCALCACHESERVER, ZNUMBEROFBYTESTOHASH, ZPERSISTENTIDENTIFIER,
                        ZPUBLICATIONVERSION, ZSIZE, ZSTATE, ZSTOREIDENTIFIER, ZLASTSTATECHANGETIME, ZSTARTTIME,
                        ZASSETPATH, ZBUYPARAMETERS, ZCANCELDOWNLOADURL, ZCLIENTIDENTIFIER, ZCOLLECTIONARTISTNAME,
                        ZCOLLECTIONTITLE, ZDOWNLOADID, ZGENRE, ZKIND, ZPLISTPATH, ZSUBTITLE, ZTHUMBNAILIMAGEURL,
                        ZTITLE, ZTRANSACTIONIDENTIFIER, ZURL, ZFILEATTRIBUTES
                    )
                    VALUES (
                        ?, 2, 3, 0, 0, 0,
                        0, 0, 0, 0,
                        0, 0, 2, 765107108, 767991550.119197, 767991353.245275,
                        ?, ?, ?, ?, 'idk',
                        ?, ?, 'Contemporary Romance', 'ebook', ?, 'Cartas de Amor a la Luna',
                        'https://is1-ssl.mzstatic.com/image/thumb/Publication126/v4/3d/b6/0a/3db60a65-b1a5-51c3-b306-c58870663fd3/Portada.jpg/200x200bb.jpg',
                        'Cartas de Amor a la Luna', 'J19N_PUB_190099164604738',
                        'https://www.google.com/robots.txt', ?
                    );
                    """

                    buy_params = (
                        "productType=PUB&price=0&salableAdamId=765107106&pricingParameters=PLUS&pg=default"
                        "&mtApp=com.apple.iBooks"
                        f"&mtEventTime={int(time.time() * 1000)}"
                        f"&mtOsVersion={_get_ios_version(lockdown_client) or '0.0'}"
                        "&mtPageId=SearchIncrementalTopResults&mtPageType=Search&mtPageContext=search"
                        "&mtTopic=xp_amp_bookstore"
                        f"&mtRequestId={uuid_mod.uuid4()}"
                    )
                    cancel_url = "https://p19-buy.itunes.apple.com/WebObjects/MZFastFinance.woa/wa/songDownloadDone?download-id=J19N_PUB_190099164604738&cancel=1"
                    client_id = "4GG2695MJK.com.apple.iBooks"

                    for f in files:
                        if getattr(f, "domain", None) not in ("", None):
                            continue

                        _, file_name = os.path.split(getattr(f, "restore_path", ""))
                        if not file_name:
                            continue

                        contents = getattr(f, "contents", b"") or b""
                        if len(contents) > 0:
                            backpath = "../../../../../.."
                            zassetpath = f"{f.restore_path}.zassetpath"
                        else:
                            backpath = ""
                            zassetpath = f.restore_path

                        # Normalize for the path stored in the db.
                        if str(f.restore_path).startswith("/"):
                            backpath += str(f.restore_path)
                        else:
                            backpath += f"/{f.restore_path}"

                        z_id += 1
                        expected_overwrites += 1
                        media_folder = f"{nugget_media_folder}/{file_name}"
                        media_file_path = f"/var/mobile/Media/{media_folder}"

                        dl_cur.execute(
                            insert_sql,
                            (
                                z_id,
                                zassetpath,
                                buy_params,
                                cancel_url,
                                client_id,
                                f"{file_name} file",
                                backpath,
                                media_file_path,
                                sqlite3.Binary(attr_data),
                            ),
                        )

                        # Upload payload file into Media (AFC root is /var/mobile/Media).
                        try:
                            afc.set_file_contents(media_folder, contents)
                        except Exception as e:
                            raise NuggetException("Failed to upload payload file via AFC.", detailed_text=repr(e))

                    dl_conn.commit()

            # Upload downloads db (+ sidecars if present)
            def fast_upload(local_path: str, remote_path: str):
                if not os.path.exists(local_path):
                    return
                try:
                    with open(local_path, "rb") as fp:
                        afc.set_file_contents(remote_path, fp.read())
                except Exception:
                    pass

            # Ensure Downloads folder exists (best-effort)
            try:
                if not afc.exists("Downloads"):
                    afc.makedirs("Downloads")
            except Exception:
                pass

            fast_upload(temp_db_path, "Downloads/downloads.28.sqlitedb")
            fast_upload(temp_db_path + "-shm", "Downloads/downloads.28.sqlitedb-shm")
            fast_upload(temp_db_path + "-wal", "Downloads/downloads.28.sqlitedb-wal")

        finally:
            # cleanup temp dir (downloads db)
            try:
                remove_db_files(temp_db_path)
            except Exception:
                pass
            try:
                shutil.rmtree(run_tmp_dir, ignore_errors=True)
            except Exception:
                pass

        # Kick itunesstored so it re-processes downloads.
        _kill_if_running(pc, _get_pid_by_name(lockdown_client, "itunesstored"))

        progress_callback("Waiting for itunesstored to finish download...\n(This might take a minute)")

        def _itunesstored_pred(entry):
            fname = posixpath.basename(getattr(entry, "filename", "") or "")
            msg = getattr(entry, "message", "") or ""
            if fname != "itunesstored":
                return False
            # Match broadly (avoid hardcoding a download id).
            return ("Install complete for download:" in msg) and ("result:" in msg)

        hit = _wait_for_syslog(lockdown_client, _itunesstored_pred, ITUNESSTORED_WAIT_TIMEOUT_S)
        if not hit:
            raise NuggetException("Timed out waiting for download. Please try again.")

        # Restart book services
        _kill_if_running(pc, _get_pid_by_name(lockdown_client, "bookassetd"))
        _kill_if_running(pc, _get_pid_by_name(lockdown_client, "Books"))

        _launch_app(pc, "com.apple.iBooks")

        progress_callback("Waiting for file overwrite to complete...\n(This might take a minute)")
        success_message = "[Install-Mgr]: Marking download as [finished]"
        num_replaced = 0

        overwrite_timeout = OVERWRITE_WAIT_TIMEOUT_S_ONDEVICE
        if transfer_mode == BookRestoreFileTransferMethod.LocalHost:
            overwrite_timeout = OVERWRITE_WAIT_TIMEOUT_S_LOCALHOST

        deadline = time.time() + overwrite_timeout
        for entry in OsTraceService(lockdown=lockdown_client).syslog():
            if time.time() > deadline:
                break
            fname = getattr(entry, "filename", "") or ""
            msg = getattr(entry, "message", "") or ""
            if str(fname).endswith("bookassetd") and success_message in msg:
                num_replaced += 1
                print(f"files finished: {num_replaced}\nmsg: {msg}")
                if transfer_mode != BookRestoreFileTransferMethod.LocalHost:
                    # on-device mode doesn't have a reliable count
                    break
                if expected_overwrites and num_replaced >= expected_overwrites:
                    break

        # Respring
        progress_callback("Respringing")
        _kill_if_running(pc, _get_pid_by_name(lockdown_client, "backboardd"))

    finally:
        # Always clean up local server + firewall rule.
        if fw_rule:
            _netsh_delete_firewall_rule(fw_rule)
        if http_server:
            http_server.stop()
        # Remove served db artifacts (LocalHost only)
        if transfer_mode == BookRestoreFileTransferMethod.LocalHost:
            try:
                remove_db_files(os.path.join(br_files, "tmp.BLDatabaseManager.sqlite"))
            except Exception:
                pass


def perform_bookrestore(
    files: list[FileToRestore],
    lockdown_client: LockdownClient,
    current_device_books_uuid_callback: Callable[..., Optional[str]] = lambda *args, **kwargs: None,
    progress_callback: Callable[[str], None] = lambda x: None,
    transfer_mode: BookRestoreFileTransferMethod = BookRestoreFileTransferMethod.LocalHost,
):
    # Developer Mode requirement (per Nugget behavior)
    if not lockdown_client.developer_mode_status:
        progress_callback("Enabling Developer Mode...")
        AmfiService(lockdown=lockdown_client).reveal_developer_mode_option_in_ui()
        raise NuggetException(
            "You must enable developer mode on your device. You can do it in the Settings app.\n\nClick \"Show Details\" for more information.",
            detailed_text=(
                "BookRestore tweaks with the AFC method require developer mode to apply.\n\n"
                "You can enable this at the bottom of Settings > Privacy & Security > Developer Mode on your iPhone or iPad."
            ),
        )

    # Must be set before creating an event loop (Windows quirk).
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # Use safe runner (works even if called from a GUI with an existing event loop).
    _run_coro_blocking(
        create_connection_context(
            files,
            lockdown_client,
            current_device_books_uuid_callback,
            progress_callback,
            transfer_mode,
        )
    )
