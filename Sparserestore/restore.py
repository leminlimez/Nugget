from . import backup, perform_restore
from pymobiledevice3.lockdown import LockdownClient
import os

class FileToRestore:
    def __init__(self, contents: str, restore_path: str, owner: int = 501, group: int = 501):
        self.contents = contents
        self.restore_path = restore_path
        self.owner = owner
        self.group = group

# files is a list of FileToRestore objects
def restore_files(files: list, reboot: bool = False, lockdown_client: LockdownClient = None):
    # create the files to be backed up
    files_list = [
    ]
    sorted_files = sorted(files, key=lambda x: x.restore_path, reverse=True)
    # add the file paths
    last_domain = ""
    for file in sorted_files:
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
        if last_domain != domain_path:
            files_list.append(backup.Directory(
                "",
                f"{domain_path}/",
                owner=file.owner,
                group=file.group
            ))
            last_domain = domain_path
        files_list.append(backup.ConcreteFile(
            "",
            f"{domain_path}/{name}",
            owner=file.owner,
            group=file.group,
            contents=file.contents
        ))
    files_list.append(backup.ConcreteFile("", "SysContainerDomain-../../../../../../../.." + "/crash_on_purpose", contents=b""))

    # create the backup
    back = backup.Backup(files=files_list)

    perform_restore(backup=back, reboot=reboot, lockdown_client=lockdown_client)


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