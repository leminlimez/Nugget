import os
import traceback
import uuid

from PySide6 import QtWidgets

from ...tweak_classes import Tweak
from ..template_file import TemplateFile

from restore.restore import FileToRestore
from exceptions.posterboard_exceptions import PBTemplateException

class TemplatesTweak(Tweak):
    def __init__(self):
        super().__init__(key=None)
        self.templates: list[TemplateFile] = []

    def uses_domains(self):
        # TODO: figure out which templates use sparse restore
        return len(self.templates) > 0

    def add_template(self, file: str, version: str = None):
        try:
            new_template = TemplateFile(path=file, device_version=version)
            if new_template.domain == "com.apple.PosterBoard":
                raise PBTemplateException(file=file, message="This is a PosterBoard template. Please import it on the PosterBoard page.")
            self.templates.append(new_template)
        except Exception as e:
            print(traceback.format_exc())
            detailsBox = QtWidgets.QMessageBox()
            detailsBox.setIcon(QtWidgets.QMessageBox.Critical)
            detailsBox.setWindowTitle("Error")
            detailsBox.setText(f"Failed to load template {file}\n\n{str(e)}")
            detailsBox.exec()
        
    def recursive_add(self, domain: str,
                      files_to_restore: list[FileToRestore],
                      curr_path: str, restore_path: str = "",
                      isAdding: bool = False
        ):
        if not os.path.isdir(curr_path):
            return
        for folder in sorted(os.listdir(curr_path)):
            if folder.startswith('.') or folder == "__MACOSX":
                continue
            if isAdding:
                # randomize uuid
                # if file then add it, otherwise recursively call again
                if os.path.isfile(os.path.join(curr_path, folder)):
                    try:
                        # update plist ids if needed
                        new_contents = None
                        contents_path = os.path.join(curr_path, folder)
                        # handle for sparserestore
                        full_path = f"{restore_path}/{folder}"
                        restore_domain = domain
                        if domain.startswith("Sparserestore-"):
                            full_path = f"{domain.removeprefix("Sparserestore-")}{full_path}"
                            restore_domain = None
                        files_to_restore.append(FileToRestore(
                            contents=new_contents,
                            contents_path=contents_path,
                            restore_path=full_path,
                            domain=restore_domain
                        ))
                    except IOError:
                        print(f"Failed to open file: {folder}") # TODO: Add QDebug equivalent
                else:
                    self.recursive_add(domain, files_to_restore, os.path.join(curr_path, folder), f"{restore_path}/{folder}", isAdding)
            else:
                # look for container folder
                if folder.lower() == "container":
                    self.recursive_add(domain, files_to_restore, os.path.join(curr_path, folder), restore_path="/", isAdding=True)
                else:
                    self.recursive_add(domain, files_to_restore, os.path.join(curr_path, folder), isAdding=False)

    def apply_tweak(self, files_to_restore: list[FileToRestore], output_dir: str, version: str, update_label=lambda x: None):
        if len(self.templates) == 0:
            return
        update_label("Extracting templates...")
        # extract templates
        for template in self.templates:
            temp_dir = os.path.join(output_dir, str(uuid.uuid4()))
            os.makedirs(temp_dir)
            template.extract(output_dir=temp_dir)
            self.recursive_add(domain=template.domain, files_to_restore=files_to_restore, curr_path=temp_dir)
        update_label("Adding other tweaks...")