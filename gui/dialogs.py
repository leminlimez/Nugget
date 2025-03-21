from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout, QWidget, QToolButton, QSizePolicy
from PySide6.QtGui import QFont

from webbrowser import open_new_tab

from controllers.web_request_handler import Nugget_Repo, get_latest_version

class GestaltDialog(QDialog):
    def __init__(self, device_manager, gestalt_label, selected_file, parent=None):
        super().__init__(parent)
        self.device_manager = device_manager
        self.gestalt_label = gestalt_label
        self.selected_file = selected_file

        QBtn = (
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("The gestalt file looks like it was made for a different device.\nAre you sure you want to use this one?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

    def accept(self):
        self.device_manager.data_singleton.gestalt_path = self.selected_file
        self.gestalt_label.setText(self.selected_file)
        super().accept()


class PBHelpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        QBtn = (
            QDialogButtonBox.Ok
        )
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        layout = QVBoxLayout()
        message = QLabel("Descriptors will be under the Collections section when adding a new wallpaper.")
        layout.addWidget(message)

        imgContainer = QWidget()
        imgContainer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        imgContainer.setStyleSheet("QWidget { border: none; }")
        # tut1 = QToolButton()


class UpdateAppDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        QBtn = (
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        title = QLabel("Update Available")
        title_font = QFont()
        title_font.setBold(True)
        title.setFont(title_font)

        message_text = ""
        latest_version = get_latest_version()
        if latest_version != None:
            message_text += f"Nugget v{latest_version} is available. "
        message_text += "Would you like to go to the download on GitHub?"
        message = QLabel(message_text)

        layout.addWidget(title)
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

    def accept(self):
        # open up the repo page
        open_new_tab(f"https://github.com/{Nugget_Repo}")
        super().accept()