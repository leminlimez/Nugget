from ..page import Page
from qt.ui_mainwindow import Ui_Nugget

from tweaks.tweaks import tweaks

class FeatureFlagsPage(Page):
    def __init__(self, ui: Ui_Nugget):
        super().__init__()
        self.ui = ui

    def load_page(self):
        self.ui.clockAnimChk.toggled.connect(self.on_clockAnimChk_toggled)
        self.ui.lockscreenChk.toggled.connect(self.on_lockscreenChk_clicked)
        self.ui.photosChk.toggled.connect(self.on_photosChk_clicked)
        self.ui.aiChk.toggled.connect(self.on_aiChk_clicked)

    ## ACTIONS
    def on_clockAnimChk_toggled(self, checked: bool):
        tweaks["ClockAnim"].set_enabled(checked)
    def on_lockscreenChk_clicked(self, checked: bool):
        tweaks["Lockscreen"].set_enabled(checked)

    def on_photosChk_clicked(self, checked: bool):
        tweaks["PhotoUI"].set_enabled(checked)
    def on_aiChk_clicked(self, checked: bool):
        tweaks["AI"].set_enabled(checked)