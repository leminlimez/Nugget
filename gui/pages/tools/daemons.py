from ..page import Page
from qt.mainwindow_ui import Ui_Nugget

from tweaks.tweak_loader import load_daemons
from tweaks.tweaks import tweaks, TweakID
from tweaks.daemons_tweak import Daemon

class DaemonsPage(Page):
    def __init__(self, ui: Ui_Nugget):
        super().__init__()
        self.ui = ui

    def load_page(self):
        self.ui.modifyDaemonsChk.toggled.connect(self.on_modifyDaemonsChk_clicked)
        self.ui.thermalmonitordChk.toggled.connect(self.on_thermalmonitordChk_clicked)
        self.ui.otadChk.toggled.connect(self.on_otadChk_clicked)
        self.ui.usageTrackingAgentChk.toggled.connect(self.on_usageTrackingAgentChk_clicked)

        self.ui.gameCenterChk.toggled.connect(self.on_gameCenterChk_clicked)
        self.ui.screenTimeChk.toggled.connect(self.on_screenTimeChk_clicked)
        self.ui.clearScreenTimeAgentChk.toggled.connect(self.on_clearScreenTimeAgentChk_clicked)
        self.ui.crashReportsChk.toggled.connect(self.on_crashReportsChk_clicked)
        self.ui.atwakeupChk.toggled.connect(self.on_atwakeupChk_clicked)
        self.ui.tipsChk.toggled.connect(self.on_tipsChk_clicked)
        self.ui.vpndChk.toggled.connect(self.on_vpndChk_clicked)
        self.ui.wapicChk.toggled.connect(self.on_wapicChk_clicked)
        self.ui.healthdChk.toggled.connect(self.on_healthdChk_clicked)

        self.ui.airprintChk.toggled.connect(self.on_airprintChk_clicked)
        self.ui.assistiveTouchChk.toggled.connect(self.on_assistiveTouchChk_clicked)
        self.ui.icloudChk.toggled.connect(self.on_icloudChk_clicked)
        self.ui.hotspotChk.toggled.connect(self.on_hotspotChk_clicked)
        self.ui.passbookChk.toggled.connect(self.on_passbookChk_clicked)
        self.ui.spotlightChk.toggled.connect(self.on_spotlightChk_clicked)
        self.ui.voiceControlChk.toggled.connect(self.on_voiceControlChk_clicked)
        self.ui.nanoTimeKitChk.toggled.connect(self.on_nanoTimeKitChk_clicked)
        self.ui.diagnosticsChk.toggled.connect(self.on_diagnosticsChk_clicked)

        load_daemons()

    ## ACTIONS
    def on_modifyDaemonsChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_enabled(checked)
        self.ui.daemonsPageContent.setDisabled(not checked)

    def on_thermalmonitordChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.thermalmonitord.value, value=checked)
        if checked:
            # set the modify toggle checked so it actually applies
            self.on_modifyDaemonsChk_clicked(True)
    def on_otadChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.OTA.value, value=checked)
    def on_usageTrackingAgentChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.UsageTrackingAgent.value, value=checked)
    def on_gameCenterChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.GameCenter.value, value=checked)
    def on_screenTimeChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.ScreenTime.value, value=checked)
    def on_clearScreenTimeAgentChk_clicked(self, checked: bool):
        tweaks[TweakID.ClearScreenTimeAgentPlist].set_enabled(checked)
    def on_crashReportsChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.CrashReports.value, value=checked)
    def on_atwakeupChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.ATWAKEUP.value, value=checked)
    def on_tipsChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.Tips.value, value=checked)
    def on_vpndChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.VPN.value, value=checked)
    def on_wapicChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.ChineseLAN.value, value=checked)
    def on_healthdChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.HealthKit.value, value=checked)

    def on_airprintChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.AirPrint.value, value=checked)
    def on_assistiveTouchChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.AssistiveTouch.value, value=checked)
    def on_icloudChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.iCloud.value, value=checked)
    def on_hotspotChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.InternetTethering.value, value=checked)
    def on_passbookChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.PassBook.value, value=checked)
    def on_spotlightChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.Spotlight.value, value=checked)
    def on_voiceControlChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.VoiceControl.value, value=checked)
    def on_nanoTimeKitChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.NanoTimeKit.value, value=checked)
    def on_diagnosticsChk_clicked(self, checked: bool):
        tweaks[TweakID.Daemons].set_multiple_values(Daemon.Diagnostics.value, value=checked)
