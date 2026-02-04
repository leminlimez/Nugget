import webbrowser

from ..page import Page
from src.qt.mainwindow_ui import Ui_Nugget
from PySide6 import QtWidgets

from src.tweaks.tweaks import tweaks, TweakID

class PasscodePage(Page):
    def __init__(self, window, ui: Ui_Nugget):
        super().__init__()
        self.window = window
        self.ui = ui

    def load_page(self):
        self.ui.importPassthmBtn.clicked.connect(self.on_importPassthmBtn_clicked)
        self.ui.keySizeDrp.activated.connect(self.on_keySizeDrp_activated)
        self.ui.passthmLanguageCodeTxt.textEdited.connect(self.on_passthmLanguageCodeTxt_textEdited)
        self.ui.discoverPassthmBtn.clicked.connect(self.on_discoverPassthmBtn_clicked)

    def on_keySizeDrp_activated(self, index: int):
        tweaks[TweakID.Passcode].big_keys = (index == 0)

    def on_passthmLanguageCodeTxt_textEdited(self, txt: str):
        if len(txt) >= 2:
            tweaks[TweakID.Passcode].language_code = txt

    def on_importPassthmBtn_clicked(self):
        selected_file, _ = QtWidgets.QFileDialog.getOpenFileName(self.window, "Select Passcode Theme Files", "", "Zip Files (*.passthm)", options=QtWidgets.QFileDialog.ReadOnly)
        tweaks[TweakID.Passcode].import_passthm(path=selected_file)
        if selected_file != None and len(selected_file) > 0:
            self.ui.selectedPassthmLbl.setText(selected_file)
        else:
            self.ui.selectedPassthmLbl.setText(self.window.noneText)

    def on_discoverPassthmBtn_clicked(self):
        webbrowser.open_new_tab("https://cowabun.ga/wallpapers?section=passtheme")