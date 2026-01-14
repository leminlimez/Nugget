from ..page import Page
from qt.mainwindow_ui import Ui_Nugget

from tweaks.tweak_loader import load_featureflags
from tweaks.tweaks import tweaks, TweakID

class FeatureFlagsPage(Page):
    def __init__(self, ui: Ui_Nugget):
        super().__init__()
        self.ui = ui

    def load_page(self):
        self.ui.createFFFolderChk.toggled.connect(self.on_createFFFolderChk_toggled)
        self.ui.clockAnimChk.toggled.connect(self.on_clockAnimChk_toggled)
        self.ui.lockscreenChk.toggled.connect(self.on_lockscreenChk_clicked)
        self.ui.photosChk.toggled.connect(self.on_photosChk_clicked)
        self.ui.aiChk.toggled.connect(self.on_aiChk_clicked)
        self.ui.kioskModeChk.toggled.connect(self.on_kioskModeChk_toggled)
        self.ui.solariumFFChk.toggled.connect(self.on_solariumFFChk_toggled)
        
        load_featureflags()

    ## ACTIONS
    def on_createFFFolderChk_toggled(self, checked: bool):
        tweaks[TweakID.CreateBRFolders].set_enabled(checked)
        self.ui.createEligFolderChk.setChecked(checked)

    def on_clockAnimChk_toggled(self, checked: bool):
        tweaks[TweakID.ClockAnim].set_enabled(checked)
    def on_lockscreenChk_clicked(self, checked: bool):
        tweaks[TweakID.Lockscreen].set_enabled(checked)

    def on_photosChk_clicked(self, checked: bool):
        tweaks[TweakID.PhotoUI].set_enabled(checked)
    def on_aiChk_clicked(self, checked: bool):
        tweaks[TweakID.AI].set_enabled(checked)

    def on_kioskModeChk_toggled(self, checked: bool):
        tweaks[TweakID.KioskMode].set_enabled(checked)
    def on_solariumFFChk_toggled(self, checked: bool):
        tweaks[TweakID.SolariumFFSwiftUI].set_enabled(checked)
        tweaks[TweakID.SolariumFFSpringBoard].set_enabled(checked)
        tweaks[TweakID.SolariumFFIconServices].set_enabled(checked)