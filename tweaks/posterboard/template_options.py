import os

from enum import Enum
from dataclasses import dataclass
from typing import Optional
from shutil import rmtree

class OptionType(Enum):
    replace = "replace"
    remove = "remove"

@dataclass
class TemplateOption:
    type: OptionType
    label: str
    files: list[str]

    def apply(self, container_path: str):
        raise NotImplementedError

@dataclass
class ReplaceOption(TemplateOption):
    button_label: Optional[str]
    allowed_files: str # Qt format - ex. "Image Files (*.png)"
    required: bool
    value: Optional[str] = None # path of file selected by user

    def apply(self, container_path: str):
        if self.value == None:
            if not self.required:
                return
            elif self.required and self.value == None:
                raise Exception(f"No selected file for required option {self.label}")
        contents=None
        in_path = os.path.join(container_path, self.value)
        with open(in_path, "rb") as in_file:
            contents = in_file.read()
        for file in self.files:
            out_path = os.path.join(container_path, file)
            with open(out_path, "wb") as out_file:
                out_file.write(contents)
        del contents

@dataclass
class RemoveOption(TemplateOption):
    value: bool = False # whether or not to delete the file

    def set_option(self, checked: bool):
        self.value = checked

    def apply(self, container_path: str):
        if self.value:
            # delete files or directories
            for file in self.files:
                path = os.path.join(container_path, file)
                if os.path.isdir(path):
                    rmtree(path=path, ignore_errors=True)
                else:
                    os.remove(path=path)