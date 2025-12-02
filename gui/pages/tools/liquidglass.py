from ..page import Page
from qt.ui_mainwindow import Ui_Nugget

from tweaks.tweak_loader import load_liquidglass
from tweaks.tweaks import TweakID

class LiquidGlassPage(Page):
    def __init__(self, ui: Ui_Nugget):
        super().__init__()
        self.ui = ui

    def load_page(self):
        # Create the radio buttons where needed
        self.createRadioBtns(key=TweakID.ForceSolariumFallback, container=self.ui.forceSolariumFallbackBtns)
        self.createRadioBtns(key=TweakID.DisableSolarium, container=self.ui.disableSolariumBtns)
        self.createRadioBtns(key=TweakID.IgnoreSolariumLinkedOnCheck, container=self.ui.ignoreSolariumAppBuildBtns)

        self.createRadioBtns(key=TweakID.NoLiquidClock, container=self.ui.noLiquidClockBtns)
        self.createRadioBtns(key=TweakID.NoLiquidDock, container=self.ui.noLiquidDockBtns)

        self.createRadioBtns(key=TweakID.DisableSpecularMotion, container=self.ui.disableSpecularBtns)
        self.createRadioBtns(key=TweakID.DisableOuterRefraction, container=self.ui.disableOuterRefractionBtns)
        self.createRadioBtns(key=TweakID.DisableSolariumHDR, container=self.ui.disableSolariumHDRBtns, invert_values=True)

        load_liquidglass()