from .tweak_classes import Tweak
from Sparserestore.restore import FileToRestore, AppBundleToRestore
import os
import zipfile
from tempfile import TemporaryDirectory
from pymobiledevice3.services.installation_proxy import InstallationProxyService
from pymobiledevice3.lockdown_service_provider import LockdownServiceProvider

class PosterboardTweak(Tweak):
    def __init__(self):
        super().__init__(key=None)
        self.zip_path = None
        self.bundle_id = "com.apple.PosterBoard"

    def recursive_add(self, files_to_restore: list[FileToRestore], curr_path: str, restore_path: str = "", isAdding: bool = False):
        for folder in sorted(os.listdir(curr_path)):
            if folder.startswith('.'):
                continue
            if isAdding:
                # if file then add it, otherwise recursively call again
                if os.path.isfile(os.path.join(curr_path, folder)):
                    try:
                        with open(os.path.join(curr_path, folder), "rb") as in_file:
                            contents = in_file.read()
                            files_to_restore.append(FileToRestore(
                                contents=contents,
                                restore_path=f"{restore_path}/{folder}",
                                domain=f"AppDomain-{self.bundle_id}"
                            ))
                    except IOError:
                        print(f"Failed to open file: {folder}") # TODO: Add QDebug equivalent
                else:
                    self.recursive_add(files_to_restore, os.path.join(curr_path, folder), f"{restore_path}/{folder}", isAdding)
            else:
                # look for contents folder
                if folder == "Container":
                    self.recursive_add(files_to_restore, os.path.join(curr_path, folder), restore_path="/", isAdding=True)
                    return
                else:
                    self.recursive_add(files_to_restore, os.path.join(curr_path, folder), isAdding=False)

    def apply_tweak(self, files_to_restore: list[FileToRestore], lockdown: LockdownServiceProvider):
        # get the app container and bundle version
        pbapp = InstallationProxyService(lockdown=lockdown).get_apps(application_type="System", calculate_sizes=False)["com.apple.PosterBoard"]
        # unzip the file
        if self.zip_path == None or not self.enabled:
            return
        with TemporaryDirectory() as output_dir:
            with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
                zip_ref.extractall(output_dir)
            # first, add the files
            self.recursive_add(files_to_restore, curr_path=output_dir)
            # next, add the app bundle
            # For UUID: pymobiledevice3 apps list -t System > apps.xml
            files_to_restore.append(AppBundleToRestore(
                bundle_id="com.apple.PosterBoard",
                bundle_version=pbapp["CFBundleInfoDictionaryVersion"],
                bundle_path=pbapp["Container"],
                container_content_class="Data/Application"
            ))