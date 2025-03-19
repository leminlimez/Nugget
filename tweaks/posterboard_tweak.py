from .tweak_classes import Tweak
from Sparserestore.restore import FileToRestore
from controllers.plist_handler import set_plist_value
import os
import zipfile
import uuid
from random import randint

class PosterboardTweak(Tweak):
    def __init__(self):
        super().__init__(key=None)
        self.zip_path = None
        self.bundle_id = "com.apple.PosterBoard"
        self.resetting = False
        self.resetType = 0 # 0 for descriptor 1 for prb

    def update_plist_id(self, file_path: str, file_name: str, randomizedID: int):
        if file_name == "com.apple.posterkit.provider.descriptor.identifier":
            return str(randomizedID).encode()
        elif file_name == "com.apple.posterkit.provider.contents.userInfo":
            return set_plist_value(file=os.path.join(file_path, file_name), key="wallpaperRepresentingIdentifier", value=randomizedID)
        elif file_name == "Wallpaper.plist":
            return set_plist_value(file=os.path.join(file_path, file_name), key="identifier", value=randomizedID)
        return None
        

    def recursive_add(self,
                      files_to_restore: list[FileToRestore],
                      curr_path: str, restore_path: str = "",
                      isAdding: bool = False,
                      randomizeUUID: bool = False, randomizedID: int = None
        ):
        for folder in sorted(os.listdir(curr_path)):
            if folder.startswith('.') or folder == "__MACOSX":
                continue
            if isAdding:
                # randomize uuid
                folder_name = folder
                curr_randomized_id = randomizedID
                if randomizeUUID:
                    folder_name = str(uuid.uuid4()).upper()
                    curr_randomized_id = randint(9999, 99999)
                # if file then add it, otherwise recursively call again
                if os.path.isfile(os.path.join(curr_path, folder)):
                    try:
                        # update plist ids if needed
                        new_contents = None
                        contents_path = os.path.join(curr_path, folder)
                        if curr_randomized_id != None:
                            new_contents = self.update_plist_id(curr_path, folder, curr_randomized_id)
                            if new_contents != None:
                                contents_path = None
                        files_to_restore.append(FileToRestore(
                            contents=new_contents,
                            contents_path=contents_path,
                            restore_path=f"{restore_path}/{folder_name}",
                            domain=f"AppDomain-{self.bundle_id}"
                        ))
                    except IOError:
                        print(f"Failed to open file: {folder}") # TODO: Add QDebug equivalent
                else:
                    self.recursive_add(files_to_restore, os.path.join(curr_path, folder), f"{restore_path}/{folder_name}", isAdding, randomizedID=curr_randomized_id)
            else:
                # look for container folder
                name = folder.lower()
                if name == "container":
                    self.recursive_add(files_to_restore, os.path.join(curr_path, folder), restore_path="/", isAdding=True)
                    return
                elif name == "descriptor" or name == "descriptors":
                    self.recursive_add(
                        files_to_restore,
                        os.path.join(curr_path, folder),
                        restore_path="/Library/Application Support/PRBPosterExtensionDataStore/61/Extensions/com.apple.WallpaperKit.CollectionsPoster/descriptors",
                        isAdding=True,
                        randomizeUUID=True
                    )
                else:
                    self.recursive_add(files_to_restore, os.path.join(curr_path, folder), isAdding=False)

    def apply_tweak(self, files_to_restore: list[FileToRestore], output_dir: str):
        # unzip the file
        if not self.enabled:
            return
        if self.resetting:
            # null out the folder
            file_path = ""
            if self.resetType == 0:
                # resetting descriptors
                file_path = "/61/Extensions/com.apple.WallpaperKit.CollectionsPoster/descriptors"
            files_to_restore.append(FileToRestore(
                contents=b"",
                restore_path=f"/Library/Application Support/PRBPosterExtensionDataStore{file_path}",
                domain=f"AppDomain-{self.bundle_id}"
            ))
            return
        elif self.zip_path == None:
            return
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
        if os.name == "nt":
            # try to get past directory name limit on windows
            output_dir = "\\\\?\\" + output_dir
        # add the files
        self.recursive_add(files_to_restore, curr_path=output_dir)