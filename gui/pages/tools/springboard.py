from ..page import Page
from qt.ui_mainwindow import Ui_Nugget

from tweaks.tweak_loader import load_springboard
from tweaks.tweaks import tweaks

class SpringboardPage(Page):
    def __init__(self, ui: Ui_Nugget):
        super().__init__()
        self.ui = ui

    def load_page(self):
        self.ui.footnoteTxt.textEdited.connect(self.on_footnoteTxt_textEdited)
        self.ui.disableLockRespringChk.toggled.connect(self.on_disableLockRespringChk_clicked)
        self.ui.disableDimmingChk.toggled.connect(self.on_disableDimmingChk_clicked)
        self.ui.disableBatteryAlertsChk.toggled.connect(self.on_disableBatteryAlertsChk_clicked)
        self.ui.hideACPowerChk.toggled.connect(self.on_hideACPowerChk_clicked)
        self.ui.disableCrumbChk.toggled.connect(self.on_disableCrumbChk_clicked)
        self.ui.enableSupervisionTextChk.toggled.connect(self.on_enableSupervisionTextChk_clicked)
        self.ui.enableAirPlayChk.toggled.connect(self.on_enableAirPlayChk_clicked)
        self.ui.lockScreenAutoLockSlider.valueChanged.connect(self.on_lockScreenAutoLockSlider_valueChanged)
        
        load_springboard()

    ## ACTIONS
    def on_footnoteTxt_textEdited(self, text: str):
        tweaks["LockScreenFootnote"].set_value(text, toggle_enabled=True)
    def on_disableLockRespringChk_clicked(self, checked: bool):
        tweaks["SBDontLockAfterCrash"].set_enabled(checked)
    def on_disableDimmingChk_clicked(self, checked: bool):
        tweaks["SBDontDimOrLockOnAC"].set_enabled(checked)
    def on_disableBatteryAlertsChk_clicked(self, checked: bool):
        tweaks["SBHideLowPowerAlerts"].set_enabled(checked)
    def on_disableCrumbChk_clicked(self, checked: bool):
        tweaks["SBNeverBreadcrumb"].set_enabled(checked)
    def on_enableSupervisionTextChk_clicked(self, checked: bool):
        tweaks["SBShowSupervisionTextOnLockScreen"].set_enabled(checked)
    def on_enableAirPlayChk_clicked(self, checked: bool):
        tweaks["AirplaySupport"].set_enabled(checked)
    def on_hideACPowerChk_clicked(self, checked: bool):
        tweaks["SBHideACPower"].set_enabled(checked)
    def on_lockScreenAutoLockSlider_valueChanged(self, value: int):
        tweaks["SBMinimumLockscreenIdleTime"].set_value(value, toggle_enabled=True)
