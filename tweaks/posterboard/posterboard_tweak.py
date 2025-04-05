import os
import uuid
from random import randint
from shutil import copytree
from PySide6 import QtWidgets

from ..tweak_classes import Tweak
from .tendie_file import TendieFile
from .template_file import TemplateFile
from Sparserestore.restore import FileToRestore
from controllers.plist_handler import set_plist_value
from controllers.files_handler import get_bundle_files
from controllers import video_handler
from controllers.aar.aar import wrap_in_aar

class PosterboardTweak(Tweak):
    def __init__(self):
        super().__init__(key=None)
        self.tendies: list[TendieFile] = []
        self.templates: list[TemplateFile] = []
        self.videoThumbnail = None
        self.videoFile = None
        self.loop_video = True
        self.reverse_video = False
        self.use_foreground = False
        self.bundle_id = "com.apple.PosterBoard"
        self.resetting = False
        self.resetType = 0 # 0 for descriptor, 1 for prb, 2 for suggested photos
        self.structure_version = 61

    def verify_tendie(self, new_tendie: TendieFile, is_template: bool = False) -> bool:
        if new_tendie.descriptor_cnt + self.get_descriptor_count() <= 10:
            if is_template:
                self.templates.append(new_tendie)
            else:
                self.tendies.append(new_tendie)
            # alert if prb reset is needed
            if new_tendie.unsafe_container:
                detailsBox = QtWidgets.QMessageBox()
                detailsBox.setIcon(QtWidgets.QMessageBox.Critical)
                detailsBox.setWindowTitle("Warning")
                detailsBox.setText("NOTE: You may need to reset all wallpapers (enable Risky Options in settings) and then re-apply for this file to work.")
                detailsBox.exec()
            return True
        return False

    def add_tendie(self, file: str):
        new_tendie = TendieFile(path=file)
        return self.verify_tendie(new_tendie)
    def add_template(self, file: str):
        try:
            new_template = TemplateFile(path=file)
        except Exception as e:
            detailsBox = QtWidgets.QMessageBox()
            detailsBox.setIcon(QtWidgets.QMessageBox.Critical)
            detailsBox.setWindowTitle("Error")
            detailsBox.setText(f"Failed to load template {file}\n\n{str(e)}")
            detailsBox.exec()
            return True
        return self.verify_tendie(new_template, is_template=True)

    def get_descriptor_count(self):
        cnt = 0
        for tendie in self.tendies:
            cnt += tendie.descriptor_cnt
        return cnt

    def update_plist_id(self, file_path: str, file_name: str, randomizedID: int):
        if file_name == "com.apple.posterkit.provider.descriptor.identifier":
            return str(randomizedID).encode()
        elif file_name == "com.apple.posterkit.provider.contents.userInfo":
            return set_plist_value(file=os.path.join(file_path, file_name), key="wallpaperRepresentingIdentifier", value=randomizedID)
        elif file_name == "Wallpaper.plist":
            return set_plist_value(file=os.path.join(file_path, file_name), key="identifier", value=randomizedID)
        return None
    

    def clean_path_name(self, path: str):
        return path# re.sub('[^a-zA-Z0-9\.\/\-_ ]', '', path)
        

    def recursive_add(self,
                      files_to_restore: list[FileToRestore],
                      curr_path: str, restore_path: str = "",
                      isAdding: bool = False,
                      randomizeUUID: bool = False, randomizedID: int = None
        ):
        if not os.path.isdir(curr_path):
            return
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
                            restore_path=self.clean_path_name(f"{restore_path}/{folder_name}"),
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
                        restore_path=f"/Library/Application Support/PRBPosterExtensionDataStore/{self.structure_version}/Extensions/com.apple.WallpaperKit.CollectionsPoster/descriptors",
                        isAdding=True,
                        randomizeUUID=True
                    )
                elif name == "video-descriptor" or name == "video-descriptors":
                    self.recursive_add(
                        files_to_restore,
                        os.path.join(curr_path, folder),
                        restore_path="/Library/Application Support/PRBPosterExtensionDataStore/61/Extensions/com.apple.PhotosUIPrivate.PhotosPosterProvider/descriptors",
                        isAdding=True,
                        randomizeUUID=True
                    )
                else:
                    self.recursive_add(files_to_restore, os.path.join(curr_path, folder), isAdding=False)

    def create_live_photo_files(self, output_dir: str):
        if self.videoFile != None and not self.loop_video:
            source_dir = get_bundle_files("files/posterboard/1F20C883-EA98-4CCE-9923-0C9A01359721")
            video_output_dir = os.path.join(output_dir, "video-descriptor/1F20C883-EA98-4CCE-9923-0C9A01359721")
            copytree(source_dir, video_output_dir, dirs_exist_ok=True)
            contents_path = os.path.join(video_output_dir, "versions/0/contents/0EFB6A0F-7052-4D24-8859-AB22BADF2E93")

            # convert the video first
            video_contents = None
            if self.videoFile.endswith('.mov'):
                # no need to convert
                with open(self.videoFile, "rb") as vid:
                    video_contents = vid.read()
            else:
                # convert to mov
                video_contents = video_handler.convert_to_mov(input_file=self.videoFile)
            # now replace video
            with open(os.path.join(contents_path, "output.layerStack/portrait-layer_settling-video.MOV"), "wb") as overriding:
                overriding.write(video_contents)
            aar_path = os.path.join(contents_path, "input.segmentation/segmentation.data.aar")
            wrap_in_aar(get_bundle_files("files/posterboard/contents.plist"), video_contents, aar_path)

            # replace the heic files
            if self.videoThumbnail != None:
                del video_contents
                with open(self.videoThumbnail, "rb") as thumb:
                    thumb_contents = thumb.read()
            else:
                raise Exception("No thumbnail heic selected!")
                # get the thumbnail from the video
                thumb_contents = video_handler.get_thumbnail_from_contents(contents=video_contents)
                del video_contents
            to_override = ["input.segmentation/asset.resource/Adjusted.HEIC", "input.segmentation/asset.resource/proxy.heic", "output.layerStack/portrait-layer_background.HEIC"]
            for file in to_override:
                with open(os.path.join(contents_path, file), "wb") as overriding:
                    overriding.write(thumb_contents)
            del thumb_contents

    def create_video_loop_files(self, output_dir: str, update_label=lambda x: None):
        print(f"file: {self.videoFile}, looping: {self.loop_video}")
        if self.videoFile and self.loop_video:
            source_dir = get_bundle_files("files/posterboard/VideoCAML")
            video_output_dir = os.path.join(output_dir, "descriptor", "VideoCAML")
            copytree(source_dir, video_output_dir, dirs_exist_ok=True)
            contents_path = os.path.join(video_output_dir, "versions", "1", "contents", "9183.Custom-810w-1080h@2x~ipad.wallpaper")
            if self.use_foreground:
                # rename the foreground layer to background
                bg_path = os.path.join(contents_path, "9183.Custom_Background-810w-1080h@2x~ipad.ca")
                contents_path = os.path.join(contents_path, "9183.Custom_Floating-810w-1080h@2x~ipad.ca")
                os.rename(contents_path, bg_path)
            else:
                contents_path = os.path.join(contents_path, "9183.Custom_Background-810w-1080h@2x~ipad.ca")
            print(f"path at {contents_path}, creating caml")
            video_handler.create_caml(video_path=self.videoFile, output_file=contents_path, auto_reverses=self.reverse_video, update_label=update_label)
            
            

    def apply_tweak(self, files_to_restore: list[FileToRestore], output_dir: str, version: str, update_label=lambda x: None):
        # unzip the file
        if not self.enabled:
            return
        if version.startswith("16"):
            # iOS 16 has a different number for the structure
            self.structure_version = 59
        else:
            self.structure_version = 61
        if self.resetting:
            # null out the folder
            file_paths = []
            if self.resetType == 0:
                # resetting descriptors
                file_paths.append(f"/{self.structure_version}/Extensions/com.apple.WallpaperKit.CollectionsPoster/descriptors")
                file_paths.append(f"/{self.structure_version}/Extensions/com.apple.MercuryPoster/descriptors")
            elif self.resetType == 2:
                # resetting suggested photos
                file_paths.append(f"/{self.structure_version}/Extensions/com.apple.PhotosUIPrivate.PhotosPosterProvider/descriptors")
            else:
                file_paths.append("")
            for file_path in file_paths:
                files_to_restore.append(FileToRestore(
                    contents=b"",
                    restore_path=f"/Library/Application Support/PRBPosterExtensionDataStore{file_path}",
                    domain=f"AppDomain-{self.bundle_id}"
                ))
            return
        elif (self.tendies == None or len(self.tendies) == 0) and (self.templates == None or len(self.templates) == 0) and (self.videoFile == None):
            return
        update_label("Generating PosterBoard Video...")
        self.create_live_photo_files(output_dir)
        self.create_video_loop_files(output_dir, update_label=update_label)
        # extract tendies
        for tendie in self.tendies:
            update_label(f"Extracting tendie {tendie.name}...")
            tendie.extract(output_dir=output_dir)
        # extract templates
        for template in self.templates:
            update_label(f"Configuring template {template.name}...")
            template.extract(output_dir=output_dir)
        # add the files
        update_label("Adding tendies...")
        self.recursive_add(files_to_restore, curr_path=output_dir)
        update_label("Adding other tweaks...")
