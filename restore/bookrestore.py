import subprocess
import atexit
import asyncio
import concurrent
import sys
import os
import posixpath
import shutil
import sqlite3
import time

from .restore import FileToRestore
from controllers.files_handler import get_bundle_files
from pymobiledevice3.lockdown import LockdownClient
from pymobiledevice3.services.afc import AfcService
from pymobiledevice3.remote.remote_service_discovery import RemoteServiceDiscoveryService
from pymobiledevice3.services.dvt.dvt_secure_socket_proxy import DvtSecureSocketProxyService
from pymobiledevice3.services.dvt.instruments.process_control import ProcessControl
from pymobiledevice3.services.os_trace import OsTraceService
from tempfile import NamedTemporaryFile
from pathlib import Path

def _run_async_rsd_connection(address, port, files, progress):
    async def async_connection():
        async with RemoteServiceDiscoveryService((address, port)) as rsd:
            loop = asyncio.get_running_loop()

            def run_blocking_callback():
                with DvtSecureSocketProxyService(rsd) as dvt:
                    apply_bookrestore_files(files, rsd, dvt, progress)

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

async def create_tunnel(udid):
    # TODO: check for Windows
    tunnel_process = subprocess.Popen(f"sudo pymobiledevice3 lockdown start-tunnel --script-mode --udid {udid}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    atexit.register(exit_func, tunnel_process)
    while True:
        output = tunnel_process.stdout.readline()
        if output:
            rsd_val = output.decode().strip()
            break
        if tunnel_process.poll() is not None:
            error = tunnel_process.stderr.readlines()
            if error:
                not_connected = None
                admin_error = None
                for i in range(len(error)):
                    if (error[i].find(b'connected') > -1):
                        not_connected = True
                    if (error[i].find(b'admin') > -1):
                        admin_error = True
                if not_connected:
                    print("It seems like your device isn't connected.", error)
                elif admin_error:
                    print("It seems like you're not running this script as admin, which is required.", error)
                else:
                    print("Error opening a tunnel.", error)
                sys.exit()
            break
    rsd_str = str(rsd_val)
    print("Sucessfully created tunnel: " + rsd_str)
    return {"address": rsd_str.split(" ")[0], "port": int(rsd_str.split(" ")[1])}

def apply_bookrestore_files(files: list[FileToRestore], lockdown_client: LockdownClient, dvt: DvtSecureSocketProxyService, progress_callback = lambda x: None):
    afc = AfcService(lockdown=lockdown_client)
    pc = ProcessControl(dvt)
    # get the uuid of the container
    uuid = open("uuid.txt", "r").read().strip() if Path("uuid.txt").exists() else ""
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
            with open("uuid.txt", "w") as f:
                f.write(uuid)
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
    progress_callback("Waiting for itunesstored to finish download...")
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
    
    progress_callback("Waiting for MobileGestalt overwrite to complete...")
    success_message = "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist) [Install-Mgr]: Marking download as [finished]"
    timeout2 = time.time() + 120 # time out after a set amount of time
    for syslog_entry in OsTraceService(lockdown=lockdown_client).syslog():
        if time.time() > timeout2:
            raise Exception("Timed out waiting for file, please try again.")
        if (posixpath.basename(syslog_entry.filename) == 'bookassetd') and \
                success_message in syslog_entry.message:
            break

async def create_connection_context(files: list[FileToRestore], udid, progress_callback = lambda x: None):
    available_address = await create_tunnel(udid)
    if available_address:
        _run_async_rsd_connection(available_address["address"], available_address["port"], files, progress_callback)
    else:
        raise Exception("An error occurred getting tunnels addresses...")

def perform_bookrestore(files: list[FileToRestore], udid, progress_callback = lambda x: None):
    asyncio.run(create_connection_context(files, udid, progress_callback))