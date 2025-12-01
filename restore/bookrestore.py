from enum import Enum
import asyncio
import concurrent
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
import sys
import tempfile

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
from http.server import HTTPServer, SimpleHTTPRequestHandler

class BookRestoreApplyMethod(Enum):
    AFC = 0
    Restore = 1

class BookRestoreFileTransferMethod(Enum):
    LocalHost = 0
    OnDevice = 1

# Global Vars
info_queue = queue.Queue()
server_folder = None
br_files = get_bundle_files("files/bookrestore")

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

async def create_tunnel(udid, progress_callback = lambda x: None):
    if os.name == 'nt':
        cmd = f'"{sys.executable}" -m pymobiledevice3 lockdown start-tunnel --script-mode --udid {udid}'
        tunnel_process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        sudo_cmd = "sudo"
        if not os.geteuid() == 0:
            progress_callback('sudo_pwd')
            while not get_sudo_complete():
                time.sleep(0.5)
            pwd = get_sudo_pwd()
            if pwd:
                sudo_cmd = f"echo {pwd} | sudo -S"
                del pwd
            else:
                raise NuggetException("No administrator permission")
        tunnel_process = subprocess.Popen(f'{sudo_cmd} "{sys.executable}" -m pymobiledevice3 lockdown start-tunnel --script-mode --udid {udid}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        del sudo_cmd
        
    atexit.register(exit_func, tunnel_process)
    
    rsd_val = None
    
    while True:
        output = tunnel_process.stdout.readline()
        if output:
            line = output.decode().strip()
            if line:
                rsd_val = line
                break
            
        if tunnel_process.poll() is not None:
            error = tunnel_process.stderr.read().decode()
            if error:
                if 'connected' in error:
                    raise NuggetException("Device not connected.", detailed_text=error)
                elif 'admin' in error:
                    raise NuggetException("Admin privileges required.", detailed_text=error)
                else:
                    raise NuggetException("Tunnel Error:", detailed_text=error)
            break
    
    if rsd_val is None:
        raise NuggetException("Tunnel process ended without returning connection details. Check if device is connected/trusted.")

    rsd_str = str(rsd_val)
    print("Sucessfully created tunnel: " + rsd_str)

    try:
        address = rsd_str.split(" ")[0]
        port = int(rsd_str.split(" ")[1])
    except (IndexError, ValueError):
        raise NuggetException(f"Failed to parse tunnel output: '{rsd_str}'. Expected 'Address Port'.")
    
    return {"address": address, "port": port}

async def create_connection_context(files: list[FileToRestore], service_provider: LockdownClient,
                                    current_device_uuid_callback = lambda x: None, progress_callback = lambda x: None,
                                    transfer_mode = BookRestoreFileTransferMethod.LocalHost):
    global server_folder
    available_address = await create_tunnel(service_provider.udid, progress_callback)
    if available_address:
        old_dir = os.getcwd()
        try:
            if transfer_mode == BookRestoreFileTransferMethod.LocalHost:
                server_folder = tempfile.mkdtemp()
                os.chdir(os.path.abspath(server_folder))
            _run_async_rsd_connection(available_address["address"], available_address["port"], files, current_device_uuid_callback, progress_callback, transfer_mode)
            try:
                shutil.rmtree(server_folder)
            except:
                pass
            server_folder = None
            os.chdir(old_dir)
        except:
            try:
                shutil.rmtree(server_folder)
            except:
                pass
            server_folder = None
            os.chdir(old_dir)
            raise
    else:
        raise NuggetException("An error occurred getting tunnels addresses...")

def _run_async_rsd_connection(address, port, files, current_device_uuid_callback, progress, transfer_mode):
    async def async_connection():
        max_retries = 10
        for i in range(max_retries):
            try:
                async with RemoteServiceDiscoveryService((address, port)) as rsd:
                    loop = asyncio.get_running_loop()
                    
                    def run_blocking_callback():
                        with DvtSecureSocketProxyService(rsd) as dvt:
                            apply_bookrestore_files(files, rsd, dvt, current_device_uuid_callback, progress, transfer_mode)

                    await loop.run_in_executor(None, run_blocking_callback)
                    return # Success

            except OSError as e:
                if isinstance(e, PermissionError) or e.errno == 13:
                    raise e

                print(f"Connection attempt {i+1}/{max_retries} failed: {e}")
                if i == max_retries - 1:
                    raise
                await asyncio.sleep(1.5)

    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(asyncio.run, async_connection())
                future.result()
        else:
            loop.run_until_complete(async_connection())
    except RuntimeError:
        asyncio.run(async_connection())

def exit_func(tunnel_proc):
    tunnel_proc.terminate()

def remove_db_files(db_path):
    for ext in ["", "-shm", "-wal"]:
        fpath = db_path + ext
        if os.path.exists(fpath):
            try:
                os.remove(fpath)
            except:
                pass

def apply_bookrestore_files(files: list[FileToRestore], lockdown_client: LockdownClient, dvt: DvtSecureSocketProxyService,
                            current_device_uuid_callback = lambda x: None, progress_callback = lambda x: None,
                            transfer_mode: BookRestoreFileTransferMethod = BookRestoreFileTransferMethod.LocalHost):
    if transfer_mode == BookRestoreFileTransferMethod.LocalHost:
        # start a local http server
        http_thread = threading.Thread(target=start_http_server, daemon=True)
        http_thread.start()
        ip, port = info_queue.get()
        print(f"Hosting temporary http server on: http://{ip}:{port}/")
    
        firewall_rule_name = f"Nugget_Temp_{port}"
        if os.name == 'nt':
            try:
                subprocess.run(
                    f'netsh advfirewall firewall add rule name="{firewall_rule_name}" dir=in action=allow protocol=TCP localport={port}',
                    shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
                )
            except Exception as e:
                print(f"Warning: Could not add firewall rule: {e}")

    afc = AfcService(lockdown=lockdown_client)
    pc = ProcessControl(dvt)
    
    # Get Container UUID
    uuid = current_device_uuid_callback().strip()
    if len(uuid) < 10:
        try:
            pc.launch("com.apple.iBooks")
        except Exception as e:
            raise NuggetException("Error launching books app", detailed_text=repr(e))
        progress_callback("Please open Books app and download a book to continue.")
        for syslog_entry in OsTraceService(lockdown=lockdown_client).syslog():
            if (posixpath.basename(syslog_entry.filename) != 'bookassetd') or \
                    not "/Documents/BLDownloads/" in syslog_entry.message:
                continue
            uuid = syslog_entry.message.split("/var/containers/Shared/SystemGroup/")[1] \
                    .split("/Documents/BLDownloads")[0]
            current_device_uuid_callback(uuid)
            break
    
    sqlite_path = os.path.join(br_files, "downloads.28.sqlitedb")
    dl_manager = os.path.join(br_files, "BLDatabaseManager.sqlite")
    
    bldb_local_prefix = f"/private/var/containers/Shared/SystemGroup/{uuid}/Documents/BLDatabaseManager/BLDatabaseManager.sqlite"
    
    temp_dir = tempfile.gettempdir()
    temp_db_path = os.path.join(temp_dir, f"nugget_db_{uuid}.sqlite")
    temp_dl_manager = os.path.join(server_folder, f"tmp.BLDatabaseManager.sqlite")
    remove_db_files(temp_dl_manager)

    try:
        shutil.copyfile(sqlite_path, temp_db_path)

        connection = sqlite3.connect(temp_db_path)
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
        if transfer_mode == BookRestoreFileTransferMethod.LocalHost:
            server_prefix = f"http://{ip}:{port}"
            bldb_server_prefix = f"{server_prefix}/tmp.BLDatabaseManager.sqlite"
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

        procs = OsTraceService(lockdown=lockdown_client).get_pid_list().get("Payload")
        pid_bookassetd = next((pid for pid, p in procs.items() if p['ProcessName'] == 'bookassetd'), None)
        pid_books = next((pid for pid, p in procs.items() if p['ProcessName'] == 'Books'), None)
        if pid_bookassetd:
            pc.signal(pid_bookassetd, 19)
        if pid_books:
            pc.kill(pid_books)

        progress_callback("Uploading files...")

        # Update the download db
        if transfer_mode == BookRestoreFileTransferMethod.LocalHost:
            shutil.copyfile(dl_manager, temp_dl_manager)
            dl_connection = sqlite3.connect(temp_dl_manager)
            dl_cursor = dl_connection.cursor()
            # make sure to clear the rows so it doesn't error
            dl_cursor.execute("DELETE FROM ZBLDOWNLOADINFO")
            file_attr_path = os.path.join(br_files, "zfileattributes.plist")
            attr_data = None
            with open(file_attr_path, 'rb') as attr_file:
                attr_data = attr_file.read()
                print(len(attr_data))
            z_id = 0
            # create NuggetPayload folder
            nugget_media_folder = "NuggetPayload"
            if not afc.exists(nugget_media_folder):
                afc.makedirs(nugget_media_folder)
        for file in files:
            if not file.domain == "" and not file.domain == None:
                continue
            path, file_name = os.path.split(file.restore_path)
            print(f"including {file.restore_path}")
            media_folder = file_name
            if transfer_mode == BookRestoreFileTransferMethod.LocalHost:
                # use the local file method for mga and local server for everything else
                if file.restore_path.endswith("MobileGestalt.plist"):
                    zurl = 'https://www.google.com/robots.txt'
                    if len(file.contents) > 0:
                        zdownloadid = '../../../../../..'
                        zassetpath = f'{file.restore_path}.zassetpath'
                        media_folder = f'{nugget_media_folder}/{file_name}'
                        zplistpath = f'/var/mobile/Media/{media_folder}'
                        afc.set_file_contents(media_folder, file.contents)
                    else:
                        zdownloadid = ""
                        zassetpath = file.restore_path
                        zplistpath = file.restore_path
                    if path.startswith('/'):
                        zdownloadid += file.restore_path
                    else:
                        zdownloadid += f'/{file.restore_path}'
                else:
                    zassetpath = file.restore_path
                    zplistpath = zassetpath
                    zdownloadid = zassetpath
                    zurl = f'{server_prefix}/{file_name}'
                    # copy file to the server
                    server_path = os.path.join(server_folder, file_name)
                    with open(server_path, 'wb') as temp_write:
                        temp_write.write(file.contents)
                z_id += 1
                dl_cursor.execute(f"""
                INSERT INTO ZBLDOWNLOADINFO (Z_PK, Z_ENT, Z_OPT, ZACCOUNTIDENTIFIER, ZCLEANUPPENDING, ZFAMILYACCOUNTIDENTIFIER, ZISAUTOMATICDOWNLOAD, ZISLOCALCACHESERVER, ZNUMBEROFBYTESTOHASH, ZPERSISTENTIDENTIFIER, ZPUBLICATIONVERSION, ZSIZE, ZSTATE, ZSTOREIDENTIFIER, ZLASTSTATECHANGETIME, ZSTARTTIME, ZASSETPATH, ZBUYPARAMETERS, ZCANCELDOWNLOADURL, ZCLIENTIDENTIFIER, ZCOLLECTIONARTISTNAME, ZCOLLECTIONTITLE, ZDOWNLOADID, ZGENRE, ZKIND, ZPLISTPATH, ZSUBTITLE, ZTHUMBNAILIMAGEURL, ZTITLE, ZTRANSACTIONIDENTIFIER, ZURL, ZFILEATTRIBUTES)
                VALUES ({z_id}, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 765107108, 767991550.119197, 767991353.245275, '{zassetpath}', 'productType=PUB&price=0&salableAdamId=765107106&pricingParameters=PLUS&pg=default&mtApp=com.apple.iBooks&mtEventTime=1746298553233&mtOsVersion=18.4.1&mtPageId=SearchIncrementalTopResults&mtPageType=Search&mtPageContext=search&mtTopic=xp_amp_bookstore&mtRequestId=35276ff6-5c8b-4136-894e-b6d8fc7677b3', 'https://p19-buy.itunes.apple.com/WebObjects/MZFastFinance.woa/wa/songDownloadDone?download-id=J19N_PUB_190099164604738&cancel=1', '4GG2695MJK.com.apple.iBooks', 'idk', '{file_name} file', '{zdownloadid}', 'Contemporary Romance', 'ebook', '{zplistpath}', 'Cartas de Amor a la Luna', 'https://is1-ssl.mzstatic.com/image/thumb/Publication126/v4/3d/b6/0a/3db60a65-b1a5-51c3-b306-c58870663fd3/Portada.jpg/200x200bb.jpg', 'Cartas de Amor a la Luna', 'J19N_PUB_190099164604738', '{zurl}', (?));
                """, (sqlite3.Binary(attr_data),))
            else:
                afc.set_file_contents(media_folder, file.contents)
        if transfer_mode == BookRestoreFileTransferMethod.LocalHost:
            dl_connection.commit()
        
        def fast_upload(local_path, remote_path):
            content = b''
            if os.path.exists(local_path):
                try:
                    with open(local_path, "rb") as f:
                        content = f.read()
                except OSError:
                    content = b''
            afc.set_file_contents(remote_path, content)

        fast_upload(temp_db_path, "Downloads/downloads.28.sqlitedb")
        fast_upload(temp_db_path + "-shm", "Downloads/downloads.28.sqlitedb-shm")
        fast_upload(temp_db_path + "-wal", "Downloads/downloads.28.sqlitedb-wal")
        connection.close()

    finally:
        remove_db_files(temp_db_path)

        if os.name == 'nt':
            try:
                subprocess.run(
                    f'netsh advfirewall firewall delete rule name="{firewall_rule_name}"',
                    shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
                )
            except:
                pass

    procs = OsTraceService(lockdown=lockdown_client).get_pid_list().get("Payload")
    pid_itunesstored = next((pid for pid, p in procs.items() if p['ProcessName'] == 'itunesstored'), None)
    if pid_itunesstored:
        pc.kill(pid_itunesstored)
    
    timeout = time.time() + 120 
    progress_callback("Waiting for itunesstored to finish download..." + "\n" + "(This might take a minute)")
    for syslog_entry in OsTraceService(lockdown=lockdown_client).syslog():
        if time.time() > timeout:
            raise NuggetException("Timed out waiting for download. Please try again.")
        if (posixpath.basename(syslog_entry.filename) == 'itunesstored') and \
            "Install complete for download: 6936249076851270152 result: Failed" in syslog_entry.message:
            break

    pid_bookassetd = next((pid for pid, p in procs.items() if p['ProcessName'] == 'bookassetd'), None)
    pid_books = next((pid for pid, p in procs.items() if p['ProcessName'] == 'Books'), None)
    if pid_bookassetd:
        pc.kill(pid_bookassetd)
    if pid_books:
        pc.kill(pid_books)
    
    try:
        pc.launch("com.apple.iBooks")
    except Exception as e:
        raise NuggetException("Error launching Books app", detailed_text=repr(e))
    
    progress_callback("Waiting for file overwrite to complete..." + "\n" + "(This might take a minute)")
    success_message = "[Install-Mgr]: Marking download as [finished]"
    num_replaced = 0
    timeout_amt = 90
    if transfer_mode == BookRestoreFileTransferMethod.LocalHost:
        timeout_amt = 20
    timeout2 = time.time() + timeout_amt
    for syslog_entry in OsTraceService(lockdown=lockdown_client).syslog():
        if (syslog_entry.filename.endswith('bookassetd')) and success_message in syslog_entry.message:
            num_replaced += 1
            print(f"files found: {num_replaced}\nmsg: {syslog_entry.message}")
            if transfer_mode != BookRestoreFileTransferMethod.LocalHost or num_replaced >= z_id:
                break
        elif time.time() > timeout2:
            # respring anyway even if it is not detected that all files overwrote
            break
            # raise Exception("Timed out waiting for file, please try again.")
    pc.kill(pid_bookassetd)
    if transfer_mode == BookRestoreFileTransferMethod.LocalHost:
        dl_connection.close()
        remove_db_files(temp_dl_manager)
        
    progress_callback("Respringing")
    procs = OsTraceService(lockdown=lockdown_client).get_pid_list().get("Payload")
    pid = next((pid for pid, p in procs.items() if p['ProcessName'] == 'backboardd'), None)
    pc.kill(pid)

def perform_bookrestore(files: list[FileToRestore], lockdown_client: LockdownClient,
                        current_device_books_uuid_callback = lambda x: None, progress_callback = lambda x: None,
                        transfer_mode: BookRestoreFileTransferMethod = BookRestoreFileTransferMethod.LocalHost):
    if not lockdown_client.developer_mode_status:
        # enable developer mode
        progress_callback("Enabling Developer Mode...")
        AmfiService(lockdown=lockdown_client).enable_developer_mode()
        raise NuggetException("Developer Mode Enabled. Please refresh the device list after reboot and apply again.")
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(create_connection_context(files, lockdown_client, current_device_books_uuid_callback, progress_callback, transfer_mode))