from .tweak_classes import Tweak
from Sparserestore.restore import FileToRestore
import os
import zipfile
from tempfile import TemporaryDirectory

class PosterboardTweak(Tweak):
    def __init__(self):
        super().__init__(key=None)
        self.zip_path = None
        self.bundle_id = "com.apple.PosterBoard"
        self.resetting = False

    def recursive_add(self, files_to_restore: list[FileToRestore], curr_path: str, restore_path: str = "", isAdding: bool = False):
        for folder in sorted(os.listdir(curr_path)):
            if folder == ".DS_Store" or folder == "__MACOSX":
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

    def apply_tweak(self, files_to_restore: list[FileToRestore]):
        # unzip the file
        if not self.enabled:
            return
        if self.resetting:
            # null out the prb folder
            files_to_restore.append(FileToRestore(
                contents=b"",
                restore_path="/Library/Application Support/PRBPosterExtensionDataStore",
                domain=f"AppDomain-{self.bundle_id}"
            ))
            return
        elif self.zip_path == None:
            return
        with TemporaryDirectory() as output_dir:
            with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
                zip_ref.extractall(output_dir)
            # add the files
            self.recursive_add(files_to_restore, curr_path=output_dir)