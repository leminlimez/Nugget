from ..page import Page
from qt.mainwindow_ui import Ui_Nugget
from PySide6 import QtWidgets

from tweaks.tweaks import tweaks, TweakID

class PasscodePage(Page):
    def __init__(self, window, ui: Ui_Nugget):
        super().__init__()
        self.window = window
        self.ui = ui

    def load_page(self):
        self.ui.importPassthmBtn.clicked.connect(self.on_importPassthmBtn_clicked)

    def on_importPassthmBtn_clicked(self):
        selected_file, _ = QtWidgets.QFileDialog.getOpenFileName(self.window, "Select Passcode Theme Files", "", "Zip Files (*.passthm)", options=QtWidgets.QFileDialog.ReadOnly)
        tweaks[TweakID.Passcode].import_passthm(path=selected_file)
        if selected_file != None and len(selected_file) > 0:
            self.ui.selectedPassthmLbl.setText(selected_file)
        else:
            self.ui.selectedPassthmLbl.setText(self.window.noneText)