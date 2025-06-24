from . import TemplateOption

from exceptions.nugget_exception import NuggetException

import os
import glob
from dataclasses import dataclass
from typing import Optional
from PySide6 import QtWidgets, QtGui, QtCore

@dataclass
class ReplaceOption(TemplateOption):
    allowed_files: str # Qt format - ex. "Image Files (*.png)"
    button_label: str = "Import"
    required: bool = False
    value: Optional[str] = None # path of file selected by user
    default_preview: Optional[QtGui.QPixmap] = None # the default preview image so that it isn't lost when replacing

    def __init__(self, data: dict):
        super().__init__(data=data)
        self.allowed_files = data['allowed_files']
        if 'button_label' in data:
            self.button_label = data['button_label']
        else:
            self.button_label = f"Import {self.allowed_files}"
        if 'required' in data:
            self.required = data['required']
        self.repl_btn = None
        self.file_path_lbl = None
        self.window = None
        self.import_icon = QtGui.QIcon(":/icon/import.svg")
        self.remove_icon = QtGui.QIcon(":/icon/trash.svg")

    def update_preview(self):
        if self.preview_lbl != None:
            if self.value == None:
                # set back to default
                self.preview_lbl.setPixmap(self.default_preview)
            else:
                # set to newly selected image
                pixmap = QtGui.QPixmap(self.value)
                self.preview_lbl.setPixmap(pixmap)

    def add_potential_preview_lbls(self, lbls):
        super().add_potential_preview_lbls(lbls)
        if self.preview_lbl != None:
            self.default_preview = self.preview_lbl.pixmap()

    def create_interface(self, options_widget: QtWidgets.QWidget, options_layout: QtWidgets.QVBoxLayout):
        # replacable object
        repl_widget = QtWidgets.QWidget(options_widget)
        repl_layout = QtWidgets.QHBoxLayout(options_widget)
        repl_layout.setContentsMargins(0, 2, 0, 2)
        repl_lbl = QtWidgets.QLabel(repl_widget)
        req_label = ""
        if self.required:
            req_label = "* "
        repl_lbl.setText(f"{req_label}{self.label}")
        repl_layout.addWidget(repl_lbl)
        # button for importing files
        imp_widget = QtWidgets.QWidget(options_widget)
        imp_layout = QtWidgets.QVBoxLayout(options_widget)
        imp_widget.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.repl_btn = QtWidgets.QToolButton(imp_widget)
        self.repl_btn.setIcon(self.import_icon)
        self.repl_btn.setIconSize(QtCore.QSize(20, 20))
        self.repl_btn.setText(self.button_label)
        self.repl_btn.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.repl_btn.clicked.connect(self.on_importReplaceBtn_clicked)
        imp_layout.addWidget(self.repl_btn)
        # file path name
        self.file_path_lbl = QtWidgets.QLabel(imp_widget)
        self.file_path_lbl.hide()
        imp_layout.addWidget(self.file_path_lbl)
        imp_widget.setLayout(imp_layout)
        repl_layout.addWidget(imp_widget)
        repl_widget.setLayout(repl_layout)
        options_layout.addWidget(repl_widget)

    def on_importReplaceBtn_clicked(self):
        if self.value == None:
            # import image
            selected_file, _ = QtWidgets.QFileDialog.getOpenFileName(self.window, "Select File", "", self.allowed_files, options=QtWidgets.QFileDialog.ReadOnly)
            if selected_file != None and selected_file != "":
                self.value = selected_file
                self.file_path_lbl.setText(selected_file)
                self.file_path_lbl.show()
                self.repl_btn.setText("Remove Selected File")
                self.repl_btn.setIcon(self.remove_icon)
        else:
            # remove current image
            self.value = None
            self.file_path_lbl.hide()
            self.repl_btn.setText(self.button_label)
            self.repl_btn.setIcon(self.import_icon)
        self.update_preview()

    def apply(self, container_path: str):
        if self.value == None:
            if not self.required:
                return
            elif self.required and self.value == None:
                raise NuggetException(QtCore.QCoreApplication.tr("Error applying template:\n\nNo selected file for required option") + f" {self.label}")
        contents=None
        in_path = os.path.join(container_path, self.value)
        with open(in_path, "rb") as in_file:
            contents = in_file.read()
        for file in self.files:
            out_path = os.path.join(container_path, *file.split('/'))
            # wildcard support
            for full_path in glob.glob(out_path, recursive=True):
                with open(full_path, "wb") as out_file:
                    out_file.write(contents)
        del contents