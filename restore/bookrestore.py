import asyncio
import os
import posixpath
import shutil
import sqlite3
import time
import threading
import functools
import queue
import socket
import subprocess
import atexit
import shlex
import sys

from .restore import FileToRestore
from gui.apply_worker import get_sudo_pwd, get_sudo_complete
from controllers.files_handler import get_bundle_files
from pymobiledevice3.lockdown import LockdownClient
from pymobiledevice3.services.afc import AfcService
from pymobiledevice3.remote.remote_service_discovery import RemoteServiceDiscoveryService
from pymobiledevice3.services.dvt.dvt_secure_socket_proxy import DvtSecureSocketProxyService
from pymobiledevice3.services.dvt.instruments.process_control import ProcessControl
from pymobiledevice3.services.os_trace import OsTraceService
from tempfile import NamedTemporaryFile, gettempdir
from uuid import uuid4
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Global Vars
info_queue = queue.Queue()
tmp_fout = None
tmp_ferr = None
sq_file = None
SCRIPT_PATH = None

def set_script_path(path: str):
    global SCRIPT_PATH
    SCRIPT_PATH = path

def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()

def start_http_server():
    handler = functools.partial(SimpleHTTPRequestHandler)
    httpd = HTTPServer(("0.0.0.0", 0), handler)
    info_queue.put((get_lan_ip(), httpd.server_port))
    httpd.serve_forever()

def read_tunnel_process(tunnel_process, stdout, stderr):
    while True:
        output = stdout.readline()
        if output:
            if type(output) is bytes:
                output = output.decode()
            rsd_val = output.strip()
            break
        if tunnel_process.poll() is not None:
            error = stderr.readlines()
            if error:
                not_connected = None
                admin_error = None
                error_str = "\n"
                for i in range(len(error)):
                    msg = error[i]
                    if type(msg) is bytes:
                        msg = msg.decode()
                    error_str += msg + "\n"
                    if (msg.find('connected') > -1):
                        not_connected = True
                    if (msg.find('admin') > -1):
                        admin_error = True
                if not_connected:
                    raise Exception(f"It seems like your device isn't connected.{error_str}")
                elif admin_error:
                    raise Exception(f"It seems like you're not running this script as admin, which is required.{error_str}")
                else:
                    raise Exception(f"Error opening a tunnel.{error_str}")
            break
    rsd_str = str(rsd_val)
    print("Sucessfully created tunnel: " + rsd_str)
    return {"address": rsd_str.split(" ")[0], "port": int(rsd_str.split(" ")[1])}

async def create_tunnel(udid, progress_callback = lambda x: None):
    exe = sys.executable
    cmd = [exe]
    windows_exe_args = None
    if getattr(sys, 'frozen', False):
        # PyInstaller exe
        if sys.platform == 'win32':
            # Windows process launch command
            cmd = ['Start-Process', '-FilePath', exe, '-ArgumentList']
            windows_exe_args = f"--tunnel, {udid}"
        elif sys.platform == 'darwin' or sys.platform.startswith('linux'):
            # macOS or Linux process launch command
            cmd += ['--tunnel', udid]
    else:
        # Running via a Python command
        cmd += [f'"{SCRIPT_PATH}"', '--tunnel', udid]
    if os.name == 'nt':
        # create temp files
        global tmp_fout
        global tmp_ferr
        tmpdir = gettempdir()
        tmp_fout = os.path.join(tmpdir, str(uuid4()))
        tmp_ferr = os.path.join(tmpdir, str(uuid4()))
        with open(tmp_fout, 'w') as out_f:
            out_f.write('')
        with open(tmp_ferr, 'w') as err_f:
            err_f.write('')

        # find powershell
        pwsh = shutil.which("pwsh") 
        powershell = shutil.which("powershell")
        if pwsh:
            POWERSHELL = pwsh
        elif powershell:
            POWERSHELL = powershell
        else:
            # manually get the powershell path
            POWERSHELL = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"

        if windows_exe_args is not None:
            windows_exe_args = f'{windows_exe_args}, "{tmp_fout}", "{tmp_ferr}"'
            cmd += [windows_exe_args]
        else:
            cmd += [shlex.quote(tmp_fout), shlex.quote(tmp_ferr)]
        # arguments to run as admin
        cmd_str = " ".join(cmd)
        cmd = [
            POWERSHELL, '-Command',
            f"Start-Process {POWERSHELL!r} -Verb RunAs -Wait",
            # "-WindowStyle Hidden",
            f"-ArgumentList '-NoLogo -NoProfile -Command \"{cmd_str}\"'"
        ]
        tunnel_process = subprocess.Popen(
            cmd
        )
        atexit.register(exit_func, tunnel_process)
        with open(tmp_fout, 'r') as stdout, open(tmp_ferr, 'r') as stderr:
            return read_tunnel_process(tunnel_process, stdout, stderr)
    else:
        sudo_cmd = "sudo"
        if not os.geteuid() == 0:
            # prompt for sudo password
            progress_callback('sudo_pwd')
            while not get_sudo_complete():
                time.sleep(0.5)
            pwd = get_sudo_pwd()
            if pwd:
                sudo_cmd = f'echo {pwd} | sudo -S'
                del pwd
            else:
                raise Exception("No administrator permission")
        cmd_str = " ".join(cmd)
        tunnel_process = subprocess.Popen(f'{sudo_cmd} {cmd_str}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        del sudo_cmd
        atexit.register(exit_func, tunnel_process)
        return read_tunnel_process(tunnel_process, tunnel_process.stdout, tunnel_process.stderr)

async def create_connection_context(files: list[FileToRestore], service_provider: LockdownClient, current_device_uuid_callback = lambda x: None, progress_callback = lambda x: None):
    available_address = await create_tunnel(service_provider.udid, progress_callback)
    if available_address:
        old_dir = os.getcwd()
        try:
            os.chdir(os.path.abspath(get_bundle_files("files/bookrestore")))
            await _run_async_rsd_connection(available_address["address"], available_address["port"], files, current_device_uuid_callback, progress_callback)
            os.chdir(old_dir)
        except:
            os.chdir(old_dir)
            raise
    else:
        raise Exception("An error occurred getting tunnels addresses...")

async def _run_async_rsd_connection(address, port, files, current_device_uuid_callback, progress):
    for attempt in range(3):
        try:
            async def async_connection():
                async with RemoteServiceDiscoveryService((address, port)) as rsd:
                    loop = asyncio.get_running_loop()
                    
                    def run_blocking_callback():
                        with DvtSecureSocketProxyService(rsd) as dvt:
                            apply_bookrestore_files(files, rsd, dvt, current_device_uuid_callback, progress)
                    
                    await loop.run_in_executor(None, run_blocking_callback)

            print(f"attempt connection ({attempt + 1}/3)...")
            await async_connection()
            return

        except (ConnectionRefusedError, OSError) as e:
            print(f"tunnel connect failed: {e}")
            if attempt < 3 - 1:
                print(f"failed. wait 2 seconds...")
                await asyncio.sleep(2)
            else:
                raise Exception(f"Tunnel connection failed: {repr(e)}")

def exit_func(tunnel_proc):
    tunnel_proc.terminate()

def apply_bookrestore_files(files: list[FileToRestore], lockdown_client: LockdownClient, dvt: DvtSecureSocketProxyService, current_device_uuid_callback = lambda x: None, progress_callback = lambda x: None):
    # start a local http server
    http_thread = threading.Thread(target=start_http_server, daemon=True)
    http_thread.start()
    ip, port = info_queue.get()
    print(f"Hosting temporary http server on: http://{ip}:{port}/")

    afc = AfcService(lockdown=lockdown_client)
    pc = ProcessControl(dvt)
    # get the uuid of the container
    uuid = current_device_uuid_callback().strip()
    if len(uuid) < 10:
        try:
            pc.launch("com.apple.iBooks")
        except Exception as e:
            raise Exception(f"Error launching books app: {e}")
        progress_callback("Please open Books app and download a book to continue.")
        for syslog_entry in OsTraceService(lockdown=lockdown_client).syslog():
            if (posixpath.basename(syslog_entry.filename) != 'bookassetd') or \
                    not "/Documents/BLDownloads/" in syslog_entry.message:
                continue
            uuid = syslog_entry.message.split("/var/containers/Shared/SystemGroup/")[1] \
                    .split("/Documents/BLDownloads")[0]
            current_device_uuid_callback(uuid)
            break
    
    # modify the sqlite database
    if getattr(sys, 'frozen', False):
        br_files = get_bundle_files("files/bookrestore")
    else:
        br_files = get_bundle_files("")
    sqlite_path = os.path.join(br_files, "downloads.28.sqlitedb")
    bldb_local_prefix = f"/private/var/containers/Shared/SystemGroup/{uuid}/Documents/BLDatabaseManager/BLDatabaseManager.sqlite"
    global sq_file
    sq_file = os.path.join(gettempdir(), f'{str(uuid4())}.sqlite')
    shutil.copyfile(sqlite_path, sq_file)
    connection = sqlite3.connect(sq_file)
    cursor = connection.cursor()
    cursor.execute(f"""
    UPDATE asset
    SET local_path = CASE
        WHEN local_path LIKE '%/BLDatabaseManager.sqlite'
            THEN '{bldb_local_prefix}'
        WHEN local_path LIKE '%/BLDatabaseManager.sqlite-shm'
            THEN '{bldb_local_prefix}-shm'
        WHEN local_path LIKE '%/BLDatabaseManager.sqlite-wal'
            THEN '{bldb_local_prefix}-wal'
    END
    WHERE local_path LIKE '/private/var/containers/Shared/SystemGroup/%/Documents/BLDatabaseManager/BLDatabaseManager.sqlite%'
    """)
    bldb_server_prefix = f"http://{ip}:{port}/BLDatabaseManager.sqlite"
    cursor.execute(f"""
    UPDATE asset
    SET url = CASE
        WHEN url LIKE '%/BLDatabaseManager.sqlite'
            THEN '{bldb_server_prefix}'
        WHEN url LIKE '%/BLDatabaseManager.sqlite-shm'
            THEN '{bldb_server_prefix}-shm'
        WHEN url LIKE '%/BLDatabaseManager.sqlite-wal'
            THEN '{bldb_server_prefix}-wal'
    END
    WHERE url LIKE '%/BLDatabaseManager.sqlite%'
    """)
    connection.commit()

    # Kill bookassetd and Books processes to stop them from updating BLDatabaseManager.sqlite
    procs = OsTraceService(lockdown=lockdown_client).get_pid_list().get("Payload")
    pid_bookassetd = next((pid for pid, p in procs.items() if p['ProcessName'] == 'bookassetd'), None)
    pid_books = next((pid for pid, p in procs.items() if p['ProcessName'] == 'Books'), None)
    if pid_bookassetd:
        pc.signal(pid_bookassetd, 19)
    if pid_books:
        pc.kill(pid_books)

    progress_callback("Uploading files...")

    # TEMP: Only for mobile gestalt
    for file in files:
        if not file.restore_path.endswith("com.apple.MobileGestalt.plist"):
            continue
        file_to_send = os.path.join(gettempdir(), f'{str(uuid4())}.plist')
        with open(file_to_send, "wb") as in_file:
            in_file.write(file.contents)
        afc.push(file_to_send, "com.apple.MobileGestalt.plist")
        remove_file(file_to_send)
    
    # Upload the sqlite db
    empty_file = os.path.join(br_files, "empty.txt")
    afc.push(sq_file, "Downloads/downloads.28.sqlitedb")
    afc.push(sq_file + "-shm", "Downloads/downloads.28.sqlitedb-shm")
    afc.push(sq_file + "-wal", "Downloads/downloads.28.sqlitedb-wal")
    connection.close()

    # Kill itunesstored to trigger BLDataBaseManager.sqlite overwrite
    procs = OsTraceService(lockdown=lockdown_client).get_pid_list().get("Payload")
    pid_itunesstored = next((pid for pid, p in procs.items() if p['ProcessName'] == 'itunesstored'), None)
    if pid_itunesstored:
        pc.kill(pid_itunesstored)
    
    # Wait for itunesstored to finish download and raise an error
    timeout = time.time() + 120 # time out after a set amount of time
    progress_callback("Waiting for itunesstored to finish download..." + "\n" + "(This might take a minute)")
    for syslog_entry in OsTraceService(lockdown=lockdown_client).syslog():
        if time.time() > timeout:
            raise Exception("Timed out waiting for download. Please try again.")
        if (posixpath.basename(syslog_entry.filename) == 'itunesstored') and \
            "Install complete for download: 6936249076851270152 result: Failed" in syslog_entry.message:
            break

    # Kill bookassetd and Books processes to trigger MobileGestalt overwrite
    pid_bookassetd = next((pid for pid, p in procs.items() if p['ProcessName'] == 'bookassetd'), None)
    pid_books = next((pid for pid, p in procs.items() if p['ProcessName'] == 'Books'), None)
    if pid_bookassetd:
        pc.kill(pid_bookassetd)
    if pid_books:
        pc.kill(pid_books)
    
    # Re-open Books app
    try:
        pc.launch("com.apple.iBooks")
    except Exception as e:
        raise Exception(f"Error launching Books app: {e}")
    
    progress_callback("Waiting for MobileGestalt overwrite to complete..." + "\n" + "(This might take a minute)")
    success_message = "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist) [Install-Mgr]: Marking download as [finished]"
    timeout2 = time.time() + 90 # time out after a set amount of time
    for syslog_entry in OsTraceService(lockdown=lockdown_client).syslog():
        if (syslog_entry.filename.endswith('bookassetd')) and success_message in syslog_entry.message:
            break
        elif time.time() > timeout2:
            raise Exception("Timed out waiting for file, please try again.")
    pc.kill(pid_bookassetd)
        
    progress_callback("Respringing")
    procs = OsTraceService(lockdown=lockdown_client).get_pid_list().get("Payload")
    pid = next((pid for pid, p in procs.items() if p['ProcessName'] == 'backboardd'), None)
    pc.kill(pid)

def remove_file(name: str | None):
    if name is not None and os.path.exists(name):
        try:
            os.remove(name)
        except:
            print(f"failed to remove temporary file {name}")

def perform_bookrestore(files: list[FileToRestore], lockdown_client: LockdownClient, current_device_books_uuid_callback = lambda x: None, progress_callback = lambda x: None):
    try:
        # Force SelectorEventLoopPolicy for Windows IPv6 support
        if os.name == 'nt':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(create_connection_context(files, lockdown_client, current_device_books_uuid_callback, progress_callback))
    finally:
        global tmp_fout
        global tmp_ferr
        global sq_file
        remove_file(tmp_fout)
        remove_file(tmp_fout)
        remove_file(sq_file)
        tmp_fout = None
        tmp_ferr = None
        sq_file = None