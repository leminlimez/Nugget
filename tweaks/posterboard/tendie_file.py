import os
import uuid
import zipfile

class TendieFile:
    path: str
    name: str
    descriptor_cnt: int
    is_container: bool
    unsafe_container: bool
    loaded: bool

    def __init__(self, path: str):
        self.path = path
        self.name = os.path.basename(path)
        self.descriptor_cnt = 0
        self.is_container = False
        self.unsafe_container = False
        self.loaded = False

        # read the contents
        with zipfile.ZipFile(path, mode="r") as archive:
            for option in archive.namelist():
                if "__macosx/" in option.lower():
                    continue
                if "container" in option.lower():
                    self.is_container = True
                    # check for the unsafe file that requires prb reset
                    if "PBFPosterExtensionDataStoreSQLiteDatabase.sqlite3" in option:
                        self.unsafe_container = True
                if "descriptor/" in option.lower():
                    item = option.lower().split("descriptor/")[1]
                    if item.count('/') == 1 and item.endswith('/'):
                        self.descriptor_cnt += 1
                elif "descriptors/" in option.lower():
                    item = option.lower().split("descriptors/")[1]
                    if item.count('/') == 1 and item.endswith('/'):
                        self.descriptor_cnt += 1

    def get_icon(self):
        if self.is_container:
            # container
            return ":/icon/shippingbox.svg"
        elif self.descriptor_cnt == 1:
            # single descriptor
            return ":/icon/photo.svg"
        else:
            # multiple descriptors
            return ":/icon/photo-stack.svg"
        
    def extract(self, output_dir: str):
        zip_output = os.path.join(output_dir, str(uuid.uuid4()))
        os.makedirs(zip_output)
        with zipfile.ZipFile(self.path, 'r') as zip_ref:
            zip_ref.extractall(zip_output)