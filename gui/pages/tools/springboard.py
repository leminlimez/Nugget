from ..page import Page
from qt.mainwindow_ui import Ui_Nugget

from tweaks.tweak_loader import load_springboard
from tweaks.tweaks import tweaks, TweakID

class SpringboardPage(Page):
    def __init__(self, ui: Ui_Nugget):
        super().__init__()
        self.ui = ui

    def load_page(self):
        self.ui.footnoteTxt.textEdited.connect(self.on_footnoteTxt_textEdited)
        self.ui.lockScreenAutoLockSlider.valueChanged.connect(self.on_lockScreenAutoLockSlider_valueChanged)

        # create the radio buttons
        self.createRadioBtns(key=TweakID.AirDropDisableTimeLimit, container=self.ui.airdropTimeLimitBtns)
        self.createRadioBtns(key=TweakID.SBDontLockAfterCrash, container=self.ui.disableLockRespringBtns)
        self.createRadioBtns(key=TweakID.SBDontDimOrLockOnAC, container=self.ui.disableDimmingBtns)
        self.createRadioBtns(key=TweakID.SBHideLowPowerAlerts, container=self.ui.lowBatteryAlertsBtns)
        self.createRadioBtns(key=TweakID.SBHideACPower, container=self.ui.hideACPowerBtns)
        self.createRadioBtns(key=TweakID.SBNeverBreadcrumb, container=self.ui.disableCrumbBtns)
        self.createRadioBtns(key=TweakID.SBShowSupervisionTextOnLockScreen, container=self.ui.supervisionTextBtns)
        self.createRadioBtns(key=TweakID.AirplaySupport, container=self.ui.enableAirPlayBtns)
        self.createRadioBtns(key=TweakID.SBAlwaysShowSystemApertureInSnapshots, container=self.ui.showDIInScreenshotsBtns)

        self.createRadioBtns(key=TweakID.SBShowAuthenticationEngineeringUI, container=self.ui.authEngUIBtns)
        self.createRadioBtns(key=TweakID.UseFloatingTabBar, container=self.ui.floatingTabBarBtns, invert_values=True)
        
        load_springboard()

    ## ACTIONS
    def on_footnoteTxt_textEdited(self, text: str):
        tweaks[TweakID.LockScreenFootnote].set_value(text, toggle_enabled=True)
    def on_lockScreenAutoLockSlider_valueChanged(self, value: int):
        self.ui.lockScreenAutoLockValueLabel.setText(f'{value}s')
        tweaks[TweakID.SBMinimumLockscreenIdleTime].set_value(value, toggle_enabled=True)
