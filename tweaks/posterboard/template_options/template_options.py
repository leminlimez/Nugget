from enum import Enum
from dataclasses import dataclass
from shutil import rmtree
from typing import Optional
from PySide6.QtWidgets import QVBoxLayout, QWidget, QLabel

class OptionType(Enum):
    replace = "replace"
    remove = "remove"
    set = "set"
    picker = "picker"

@dataclass
class TemplateOption:
    type: OptionType
    label: str
    files: list[str]
    associated_preview: Optional[str]
    preview_lbl: Optional[QLabel]

    def __init__(self, data: dict):
        self.type = OptionType[data['type']]
        self.label = data['label']
        if self.type == OptionType.picker:
            # picker should not have files
            self.files = []
        else:
            self.files = data['files']
        if 'associated_preview' in data:
            self.associated_preview = data['associated_preview']
        else:
            self.associated_preview = None
        self.preview_lbl = None

    def add_potential_preview_lbls(self, lbls: dict[str, QLabel]):
        if self.associated_preview != None and self.associated_preview in lbls:
            self.preview_lbl = lbls[self.associated_preview]
    def update_preview(self):
        pass

    def create_interface(self, options_widget: QWidget, options_layout: QVBoxLayout):
        raise NotImplementedError

    def apply(self, container_path: str):
        raise NotImplementedError