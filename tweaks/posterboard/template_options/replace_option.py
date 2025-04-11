from . import TemplateOption

import os
from dataclasses import dataclass
from typing import Optional

@dataclass
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