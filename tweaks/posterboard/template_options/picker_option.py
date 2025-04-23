from . import TemplateOption

import os
from dataclasses import dataclass
from shutil import rmtree, move
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox

from controllers.xml_handler import delete_xml_value
from gui.multicombobox import MultiComboBox

class PickerElement:
    label: str # label to show for the picker
    files: list[str] = [] # list of files to include with the picker

    def __init__(self, option_data: dict):
        self.label = option_data['label']
        if 'files' in option_data:
            self.files = option_data['files']

class PickerOption(TemplateOption):
    options: list[PickerElement] # list of elements inside the picker
    allow_multiple_selection: bool = False # allow choosing multiple options
    rename: bool = False # whether or not to rename the chosen files (allow_multiple_selection must be False)
    names: list[str] = [] # list of names to rename to

    selection: int|list[str] = [] # chosen user selection

    def __init__(self, data: dict):
        super().__init__(data=data)
        # get the list of options
        self.options = []
        opts = data['options']
        for opt in opts:
            self.options.append(PickerElement(opt))
        
        # add the other options
        if 'allow_multiple_selection' in data:
            self.allow_multiple_selection = data['allow_multiple_selection']
        if not self.allow_multiple_selection:
            self.selection = 0
            if 'rename' in data:
                self.rename = data['rename']
                if self.rename:
                    self.names = data['names'] # only require if rename is true

    def create_interface(self, options_widget: QWidget, options_layout: QVBoxLayout):
        # picker option
        picker_widget = QWidget(options_widget)
        picker_layout = QHBoxLayout(options_widget)
        # add label first
        picker_label = QLabel(picker_widget)
        picker_label.setText(self.label)
        picker_layout.addWidget(picker_label)
        if self.allow_multiple_selection:
            pickerDrp = MultiComboBox(picker_widget, updateAction=self.onPickerUpdate)
            for opt in self.options:
                pickerDrp.addItem(opt.label)
            pickerDrp.lineEdit().setText("  None")
            pickerDrp.setStyleSheet("QWidget { background-color: #3b3b3b; border: 2px solid #3b3b3b; border-radius: 5px; }")
        else:
            pickerDrp = QComboBox(picker_widget)
            for opt in self.options:
                pickerDrp.addItem(opt.label)
            pickerDrp.activated.connect(self.onPickerUpdate)
            pickerDrp.setCurrentIndex(0)
        picker_layout.addWidget(pickerDrp)
        picker_widget.setLayout(picker_layout)
        options_layout.addWidget(picker_widget)

    def onPickerUpdate(self, selection: int|list[str]):
        self.selection = selection

    def apply(self, container_path: str):
        # get the list of files
        sel_options: list[PickerElement] = []
        if self.allow_multiple_selection:
            for opt in self.options:
                if opt.label in self.selection:
                    sel_options.append(opt)
        else:
            sel_options.append(self.options[self.selection])
        # delete the files that are not in use
        for opt in self.options:
            if not opt in sel_options:
                for file in opt.files:
                    # delete files or directories
                    path = os.path.join(container_path, file)
                    if os.path.isdir(path):
                        rmtree(path=path, ignore_errors=True)
                    else:
                        os.remove(path=path)
        # rename the files if needed
        if self.rename:
            for i in range(len(self.options[self.selection].files)):
                # rename files or directories
                old_path = os.path.join(container_path, self.options[self.selection].files[i])
                new_path = os.path.join(container_path, self.names[i])
                if os.path.isdir(path):
                    # rename whole directory
                    move(old_path, new_path)
                else:
                    os.rename(old_path, new_path)