from ..page import Page
from qt.ui_mainwindow import Ui_Nugget

from tweaks.tweak_loader import load_internal
from tweaks.tweaks import tweaks

class InternalPage(Page):
    def __init__(self, ui: Ui_Nugget):
        super().__init__()
        self.ui = ui

    def load_page(self):
        self.ui.buildVersionChk.toggled.connect(self.on_buildVersionChk_clicked)
        self.ui.RTLChk.toggled.connect(self.on_RTLChk_clicked)
        self.ui.LTRChk.toggled.connect(self.on_LTRChk_clicked)
        self.ui.sbIconVisibilityChk.toggled.connect(self.on_sbIconVisibilityChk_clicked)
        self.ui.keyFlickChk.toggled.connect(self.on_keyFlickChk_clicked)
        self.ui.metalHUDChk.toggled.connect(self.on_metalHUDChk_clicked)
        self.ui.iMessageChk.toggled.connect(self.on_iMessageChk_clicked)
        self.ui.IDSChk.toggled.connect(self.on_IDSChk_clicked)
        self.ui.VCChk.toggled.connect(self.on_VCChk_clicked)
        self.ui.accessoryDevChk.toggled.connect(self.on_accessoryDevChk_clicked)
        self.ui.appStoreChk.toggled.connect(self.on_appStoreChk_clicked)
        self.ui.notesChk.toggled.connect(self.on_notesChk_clicked)
        self.ui.showTouchesChk.toggled.connect(self.on_showTouchesChk_clicked)
        self.ui.hideRespringChk.toggled.connect(self.on_hideRespringChk_clicked)
        self.ui.enableWakeVibrateChk.toggled.connect(self.on_enableWakeVibrateChk_clicked)
        self.ui.pasteSoundChk.toggled.connect(self.on_pasteSoundChk_clicked)
        self.ui.notifyPastesChk.toggled.connect(self.on_notifyPastesChk_clicked)

        load_internal()

    ## ACTIONS
    def on_buildVersionChk_clicked(self, checked: bool):
        tweaks["SBBuildNumber"].set_enabled(checked)
    def on_RTLChk_clicked(self, checked: bool):
        tweaks["RTL"].set_enabled(checked)
    def on_LTRChk_clicked(self, checked: bool):
        tweaks["LTR"].set_enabled(checked)
    def on_sbIconVisibilityChk_clicked(self, checked: bool):
        tweaks["SBIconVisibility"].set_enabled(checked)
    def on_keyFlickChk_clicked(self, checked: bool):
        tweaks["KeyFlick"].set_enabled(checked)
    
    def on_metalHUDChk_clicked(self, checked: bool):
        tweaks["MetalForceHudEnabled"].set_enabled(checked)
    def on_iMessageChk_clicked(self, checked: bool):
        tweaks["iMessageDiagnosticsEnabled"].set_enabled(checked)
    def on_IDSChk_clicked(self, checked: bool):
        tweaks["IDSDiagnosticsEnabled"].set_enabled(checked)
    def on_VCChk_clicked(self, checked: bool):
        tweaks["VCDiagnosticsEnabled"].set_enabled(checked)
    def on_accessoryDevChk_clicked(self, checked: bool):
        tweaks["AccessoryDeveloperEnabled"].set_enabled(checked)

    def on_appStoreChk_clicked(self, checked: bool):
        tweaks["AppStoreDebug"].set_enabled(checked)
    def on_notesChk_clicked(self, checked: bool):
        tweaks["NotesDebugMode"].set_enabled(checked)

    def on_showTouchesChk_clicked(self, checked: bool):
        tweaks["BKDigitizerVisualizeTouches"].set_enabled(checked)
    def on_hideRespringChk_clicked(self, checked: bool):
        tweaks["BKHideAppleLogoOnLaunch"].set_enabled(checked)
    def on_enableWakeVibrateChk_clicked(self, checked: bool):
        tweaks["EnableWakeGestureHaptic"].set_enabled(checked)
    def on_pasteSoundChk_clicked(self, checked: bool):
        tweaks["PlaySoundOnPaste"].set_enabled(checked)
    def on_notifyPastesChk_clicked(self, checked: bool):
        tweaks["AnnounceAllPastes"].set_enabled(checked)
