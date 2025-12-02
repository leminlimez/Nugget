from ..page import Page
from qt.ui_mainwindow import Ui_Nugget

from tweaks.tweak_loader import load_internal
from tweaks.tweaks import TweakID

class InternalPage(Page):
    def __init__(self, ui: Ui_Nugget):
        super().__init__()
        self.ui = ui

    def load_page(self):
        # Create the radio buttons where needed
        self.createRadioBtns(key=TweakID.SBBuildNumber, container=self.ui.buildVersionBtns)
        self.createRadioBtns(key=TweakID.RTL, container=self.ui.RTLBtns)
        self.createRadioBtns(key=TweakID.LTR, container=self.ui.LTRBtns)
        self.createRadioBtns(key=TweakID.SBIconVisibility, container=self.ui.sbIconVisibilityBtns)
        self.createRadioBtns(key=TweakID.KeyFlick, container=self.ui.keyFlickBtns)

        self.createRadioBtns(key=TweakID.MetalForceHudEnabled, container=self.ui.metalHUDBtns)
        self.createRadioBtns(key=TweakID.iMessageDiagnosticsEnabled, container=self.ui.iMessageBtns)
        self.createRadioBtns(key=TweakID.IDSDiagnosticsEnabled, container=self.ui.IDSBtns)
        self.createRadioBtns(key=TweakID.VCDiagnosticsEnabled, container=self.ui.VCBtns)
        self.createRadioBtns(key=TweakID.AccessoryDeveloperEnabled, container=self.ui.accessoryDevBtns)

        self.createRadioBtns(key=TweakID.AppStoreDebug, container=self.ui.appStoreBtns)
        self.createRadioBtns(key=TweakID.NotesDebugMode, container=self.ui.notesBtns)

        self.createRadioBtns(key=TweakID.BKDigitizerVisualizeTouches, container=self.ui.showTouchesBtns)
        self.createRadioBtns(key=TweakID.BKHideAppleLogoOnLaunch, container=self.ui.hideRespringBtns)
        self.createRadioBtns(key=TweakID.EnableWakeGestureHaptic, container=self.ui.wakeVibrateBtns)
        self.createRadioBtns(key=TweakID.PlaySoundOnPaste, container=self.ui.pasteSoundBtns)
        self.createRadioBtns(key=TweakID.AnnounceAllPastes, container=self.ui.notifyPastesBtns)

        load_internal()
