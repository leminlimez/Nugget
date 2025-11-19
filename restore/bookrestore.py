import asyncio
import concurrent
import os
import posixpath
import shutil
import sqlite3
import time
import threading
import sys

from .restore import FileToRestore
from . import reboot_device
from controllers.files_handler import get_bundle_files
from pymobiledevice3.lockdown import LockdownClient
from pymobiledevice3.services.afc import AfcService
from pymobiledevice3.remote.remote_service_discovery import RemoteServiceDiscoveryService
from pymobiledevice3.services.dvt.dvt_secure_socket_proxy import DvtSecureSocketProxyService
from pymobiledevice3.services.dvt.instruments.process_control import ProcessControl
from pymobiledevice3.services.os_trace import OsTraceService
from pymobiledevice3.cli.remote import start_tunnel_task, ConnectionType
from pymobiledevice3.cli.lockdown import async_cli_start_tunnel
from tempfile import NamedTemporaryFile
from io import StringIO

# Global Vars
should_terminate_tunnel = False
rsd_info = None
thread_exception = None

async def create_tunnel_async(service_provider: LockdownClient):
    global thread_exception
    thread_exception = None
    try:
        if os.name == 'nt':
            task = asyncio.create_task(async_cli_start_tunnel(service_provider, script_mode=True))
        else:
            task = asyncio.create_task(start_tunnel_task(connection_type=ConnectionType.USB, secrets=None, udid=service_provider.udid, script_mode=True))
        while not terminate_tunnel_thread:
            await asyncio.sleep(1)
        task.cancel()
    except Exception as e:
        thread_exception = e
        return

def create_tunnel(service_provider: LockdownClient):
    asyncio.run(create_tunnel_async(service_provider))

def check_rsd_info(stdout):
    global rsd_info
    MAX_ATTEMPTS = 30
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        output = stdout.getvalue()
        if output:
            rsd_val = output.strip()
            rsd_info = {"address": rsd_val.split(" ")[0], "port": int(rsd_val.split(" ")[1])}
            return True # Data is available
        if thread_exception is not None:
            return False # Thread returned an error
        time.sleep(1)
        attempts += 1
    return False

async def create_connection_context(files: list[FileToRestore], service_provider: LockdownClient, current_device_uuid_callback = lambda x: None, progress_callback = lambda x: None):
    global terminate_tunnel_thread
    global rsd_info
    global thread_exception
    terminate_tunnel_thread = False
    rsd_info = None
    thread_exception = None

    old_stdout = sys.stdout
    # redirect stdout
    redir_stdout = StringIO()
    sys.stdout = redir_stdout
    thread = threading.Thread(target=create_tunnel, args=(service_provider,))
    thread.start()
    try:
        if check_rsd_info(redir_stdout):
            sys.stdout = old_stdout
            _run_async_rsd_connection(rsd_info["address"], rsd_info["port"], files, current_device_uuid_callback, progress_callback)
        else:
            if thread_exception is not None:
                raise thread_exception
            else:
                raise Exception("An error occurred getting tunnels addresses...")
    except:
        terminate_tunnel_thread = True
        sys.stdout = old_stdout
        raise
    terminate_tunnel_thread = True

def _run_async_rsd_connection(address, port, files, current_device_uuid_callback, progress):
    async def async_connection():
        async with RemoteServiceDiscoveryService((address, port)) as rsd:
            loop = asyncio.get_running_loop()

            def run_blocking_callback():
                with DvtSecureSocketProxyService(rsd) as dvt:
                    apply_bookrestore_files(files, rsd, dvt, current_device_uuid_callback, progress)

            await loop.run_in_executor(None, run_blocking_callback)

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

def apply_bookrestore_files(files: list[FileToRestore], lockdown_client: LockdownClient, dvt: DvtSecureSocketProxyService, current_device_uuid_callback = lambda x: None, progress_callback = lambda x: None):
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
    br_files = get_bundle_files("files/bookrestore")
    sqlite_path = os.path.join(br_files, "downloads.28.sqlitedb")
    with NamedTemporaryFile("rb+", suffix=".sqlite") as sq_file:
        shutil.copyfile(sqlite_path, sq_file.name)
        connection = sqlite3.connect(sq_file.name)
        cursor = connection.cursor()
        cursor.execute(f"""
        UPDATE asset
        SET local_path = CASE
            WHEN local_path LIKE '/private/var/containers/Shared/SystemGroup/%/Documents/BLDatabaseManager/BLDatabaseManager.sqlite'
                THEN '/private/var/containers/Shared/SystemGroup/{uuid}/Documents/BLDatabaseManager/BLDatabaseManager.sqlite'
            WHEN local_path LIKE '/private/var/containers/Shared/SystemGroup/%/Documents/BLDatabaseManager/BLDatabaseManager.sqlite-shm'
                THEN '/private/var/containers/Shared/SystemGroup/{uuid}/Documents/BLDatabaseManager/BLDatabaseManager.sqlite-shm'
            WHEN local_path LIKE '/private/var/containers/Shared/SystemGroup/%/Documents/BLDatabaseManager/BLDatabaseManager.sqlite-wal'
                THEN '/private/var/containers/Shared/SystemGroup/{uuid}/Documents/BLDatabaseManager/BLDatabaseManager.sqlite-wal'
        END
        WHERE local_path LIKE '/private/var/containers/Shared/SystemGroup/%/Documents/BLDatabaseManager/BLDatabaseManager.sqlite%'
        """)
        connection.commit()
        connection.close()

        # Kill bookassetd and Books processes to stop them from updating BLDatabaseManager.sqlite
        procs = OsTraceService(lockdown=lockdown_client).get_pid_list().get("Payload")
        pid_bookassetd = next((pid for pid, p in procs.items() if p['ProcessName'] == 'bookassetd'), None)
        pid_books = next((pid for pid, p in procs.items() if p['ProcessName'] == 'Books'), None)
        if pid_bookassetd:
            pc.kill(pid_bookassetd)
        if pid_books:
            pc.kill(pid_books)

        progress_callback("Uploading files...")

        # TEMP: Only for mobile gestalt
        for file in files:
            if not file.restore_path.endswith("com.apple.MobileGestalt.plist"):
                continue
            with NamedTemporaryFile("wb", suffix=".plist") as in_file:
                in_file.write(file.contents)
                afc.push(in_file.name, "com.apple.MobileGestalt.plist")
        
        # Upload the sqlite db
        empty_file = os.path.join(br_files, "empty.txt")
        afc.push(sq_file.name, "Downloads/downloads.28.sqlitedb")
        afc.push(empty_file, "Downloads/downloads.28.sqlitedb-shm")
        afc.push(empty_file, "Downloads/downloads.28.sqlitedb-wal")

    # Kill itunesstored to trigger BLDataBaseManager.sqlite overwrite
    procs = OsTraceService(lockdown=lockdown_client).get_pid_list().get("Payload")
    pid_itunesstored = next((pid for pid, p in procs.items() if p['ProcessName'] == 'itunesstored'), None)
    if pid_itunesstored:
        pc.kill(pid_itunesstored)
    
    # Wait for itunesstored to finish download and raise an error
    timeout = time.time() + 90 # time out after a set amount of time
    progress_callback("Waiting for itunesstored to finish download..." + "\n" + "(This might take a minute)")
    for syslog_entry in OsTraceService(lockdown=lockdown_client).syslog():
        if time.time() > timeout:
            raise Exception("Timed out waiting for download. Please reboot and try again.")
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
            raise Exception("Timed out waiting for file, please reboot and try again.")
        
    progress_callback("Respringing")
    procs = OsTraceService(lockdown=lockdown_client).get_pid_list().get("Payload")
    pid = next((pid for pid, p in procs.items() if p['ProcessName'] == 'backboardd'), None)
    pc.kill(pid)

def perform_bookrestore(files: list[FileToRestore], lockdown_client: LockdownClient, current_device_books_uuid_callback = lambda x: None, progress_callback = lambda x: None):
    asyncio.run(create_connection_context(files, lockdown_client, current_device_books_uuid_callback, progress_callback))