from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QToolButton, QSizePolicy
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtCore import QSize

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
        message = QLabel(self.tr("The gestalt file looks like it was made for a different device.\nAre you sure you want to use this one?"))
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
        self.setWindowTitle(self.tr("PosterBoard Info"))

        layout = QVBoxLayout()
        message = QLabel(self.tr("Descriptors will be under the Collections section when adding a new wallpaper.\n\nIf the wallpapers don't appear in the menu, you either have to wait a bit for them to load,\nor you've reached the maximum amount of wallpapers (15) and have to wipe them."))
        layout.addWidget(message)

        imgBox = QWidget()
        imgBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        imgBox.setStyleSheet("QWidget { background: none; padding: 0px; border: none; }")
        hlayout = QHBoxLayout()
        tut1 = QToolButton()
        tut1.setIconSize(QSize(138, 300))
        tut1.setStyleSheet("QToolButton { background: none; padding: 0px; border: none; }")
        tut1.setIcon(QIcon(QPixmap(":/gui/pb_tutorial1.png")))
        hlayout.addWidget(tut1)
        tut2 = QToolButton()
        tut2.setIconSize(QSize(138, 300))
        tut2.setStyleSheet("QToolButton { background: none; padding: 0px; border: none; }")
        tut2.setIcon(QIcon(QPixmap(":/gui/pb_tutorial2.png")))
        hlayout.addWidget(tut2)
        imgBox.setLayout(hlayout)

        layout.addWidget(imgBox)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)


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
        title = QLabel(self.tr("Update Available"))
        title_font = QFont()
        title_font.setBold(True)
        title.setFont(title_font)

        message_text = ""
        latest_version = get_latest_version()
        if latest_version != None:
            message_text += self.tr("Nugget v{0} is available. ").format(latest_version)
        message_text += self.tr("Would you like to go to the download on GitHub?")
        message = QLabel(message_text)

        layout.addWidget(title)
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

    def accept(self):
        # open up the repo page
        open_new_tab(f"https://github.com/{Nugget_Repo}")
        super().accept()