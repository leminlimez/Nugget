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

    def __init__(self, data: dict):
        self.type = data['type']
        self.label = data['label']
        self.files = data['files']

    def apply(self, container_path: str):
        raise NotImplementedError


class ReplaceOption(TemplateOption):
    allowed_files: str # Qt format - ex. "Image Files (*.png)"
    button_label: Optional[str] = None
    required: bool = False
    value: Optional[str] = None # path of file selected by user

    def __init__(self, data: dict):
        super().__init__(data=data)
        if 'button_label' in data:
            self.button_label = data['button_label']
        self.allowed_files = data['allowed_files']
        if 'required' in data:
            self.required = data['required']

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
    inverted: bool = False # if set to true, the files will only be deleted if the checkbox is unchecked
    default_value: bool = False # whether the checkbox starts as true or false
    value: bool = False # whether or not to delete the file

    def __init__(self, data: dict):
        super().__init__(data=data)
        if 'inverted' in data:
            self.inverted = data['inverted']
        if 'default_value' in data:
            self.default_value = data['default_value']

    def set_option(self, checked: bool):
        self.value = checked

    def apply(self, container_path: str):
        if (self.inverted and not self.value) or (not self.inverted and self.value):
            # delete files or directories
            for file in self.files:
                path = os.path.join(container_path, file)
                if os.path.isdir(path):
                    rmtree(path=path, ignore_errors=True)
                else:
                    os.remove(path=path)