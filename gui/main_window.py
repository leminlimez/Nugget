from PySide6 import QtCore, QtWidgets, QtGui
from enum import Enum
from os import name as os_name
import webbrowser
import plistlib

from pymobiledevice3.lockdown import create_using_usbmux

from qt.ui_mainwindow import Ui_Nugget

from controllers.web_request_handler import is_update_available

from devicemanagement.constants import Version
from devicemanagement.device_manager import DeviceManager

from gui.dialogs import GestaltDialog, UpdateAppDialog, PBHelpDialog

from tweaks.tweaks import tweaks
from tweaks.custom_gestalt_tweaks import CustomGestaltTweaks, ValueTypeStrings
from tweaks.daemons_tweak import Daemon

App_Version = "5.0.1"
App_Build = 1

class Page(Enum):
    Home = 0
    Gestalt = 1
    FeatureFlags = 2
    EUEnabler = 3
    Springboard = 4
    InternalOptions = 5
    Daemons = 6
    Posterboard = 7
    RiskyTweaks = 8
    Apply = 9
    Settings = 10

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, device_manager: DeviceManager):
        super(MainWindow, self).__init__()
        self.device_manager = device_manager
        self.ui = Ui_Nugget()
        self.ui.setupUi(self)
        self.show_uuid = False
        self.pb_mainLayout = None
        self.loadSettings()

        # Check for an update
        if is_update_available(App_Version, App_Build):
            # notify with prompt to download the new version from github
            UpdateAppDialog().exec()
        # Update the app version/build number label
        self.updateAppVersionLabel()

        ## DEVICE BAR
        self.refresh_devices()

        self.ui.refreshBtn.clicked.connect(self.refresh_devices)
        self.ui.devicePicker.currentIndexChanged.connect(self.change_selected_device)

        ## SIDE BAR ACTIONS
        self.ui.homePageBtn.clicked.connect(self.on_homePageBtn_clicked)
        self.ui.gestaltPageBtn.clicked.connect(self.on_gestaltPageBtn_clicked)
        self.ui.featureFlagsPageBtn.clicked.connect(self.on_featureFlagsPageBtn_clicked)
        self.ui.euEnablerPageBtn.clicked.connect(self.on_euEnablerPageBtn_clicked)
        self.ui.springboardOptionsPageBtn.clicked.connect(self.on_springboardOptionsPageBtn_clicked)
        self.ui.internalOptionsPageBtn.clicked.connect(self.on_internalOptionsPageBtn_clicked)
        self.ui.daemonsPageBtn.clicked.connect(self.on_daemonsPageBtn_clicked)
        self.ui.posterboardPageBtn.clicked.connect(self.on_posterboardPageBtn_clicked)
        self.ui.advancedPageBtn.clicked.connect(self.on_advancedPageBtn_clicked)
        self.ui.applyPageBtn.clicked.connect(self.on_applyPageBtn_clicked)
        self.ui.settingsPageBtn.clicked.connect(self.on_settingsPageBtn_clicked)

        ## HOME PAGE ACTIONS
        self.ui.phoneVersionLbl.linkActivated.connect(self.toggle_version_label)

        ## HOME PAGE LINKS
        self.ui.bigNuggetBtn.clicked.connect(self.on_bigNuggetBtn_clicked)
        self.ui.starOnGithubBtn.clicked.connect(self.on_githubBtn_clicked)

        self.ui.leminGithubBtn.clicked.connect(self.on_leminGitHubBtn_clicked)
        self.ui.leminTwitterBtn.clicked.connect(self.on_leminTwitterBtn_clicked)
        self.ui.leminKoFiBtn.clicked.connect(self.on_leminKoFiBtn_clicked)
        
        self.ui.posterRestoreBtn.clicked.connect(self.on_posterRestoreBtn_clicked)
        self.ui.disfordottieBtn.clicked.connect(self.on_disfordottieBtn_clicked)
        self.ui.mikasaBtn.clicked.connect(self.on_mikasaBtn_clicked)

        self.ui.libiBtn.clicked.connect(self.on_libiBtn_clicked)
        self.ui.jjtechBtn.clicked.connect(self.on_jjtechBtn_clicked)
        self.ui.qtBtn.clicked.connect(self.on_qtBtn_clicked)

        self.ui.discordBtn.clicked.connect(self.on_discordBtn_clicked)

        ## ELIGIBILITY PAGE ACTIONS
        self.ui.euEnablerEnabledChk.toggled.connect(self.on_euEnablerEnabledChk_toggled)
        self.ui.methodChoiceDrp.activated.connect(self.on_methodChoiceDrp_activated)
        self.ui.regionCodeTxt.textEdited.connect(self.on_regionCodeTxt_textEdited)

        self.ui.enableAIChk.toggled.connect(self.on_enableAIChk_toggled)
        self.ui.eligFileChk.toggled.connect(self.on_eligFileChk_toggled)
        self.ui.languageTxt.hide() # to be removed later
        self.ui.languageLbl.hide() # to be removed later
        self.ui.languageTxt.textEdited.connect(self.on_languageTxt_textEdited)
        self.ui.spoofedModelDrp.activated.connect(self.on_spoofedModelDrp_activated)
        self.ui.spoofHardwareChk.toggled.connect(self.on_spoofHardwareChk_toggled)
        self.ui.spoofCPUChk.toggled.connect(self.on_spoofCPUChk_toggled)

        ## FEATURE FLAGS PAGE
        self.ui.clockAnimChk.toggled.connect(self.on_clockAnimChk_toggled)
        self.ui.lockscreenChk.toggled.connect(self.on_lockscreenChk_clicked)
        self.ui.photosChk.toggled.connect(self.on_photosChk_clicked)
        self.ui.aiChk.toggled.connect(self.on_aiChk_clicked)

        ## SPRINGBOARD OPTIONS PAGE ACTIONS
        self.ui.footnoteTxt.textEdited.connect(self.on_footnoteTxt_textEdited)
        self.ui.disableLockRespringChk.toggled.connect(self.on_disableLockRespringChk_clicked)
        self.ui.disableDimmingChk.toggled.connect(self.on_disableDimmingChk_clicked)
        self.ui.disableBatteryAlertsChk.toggled.connect(self.on_disableBatteryAlertsChk_clicked)
        self.ui.disableCrumbChk.toggled.connect(self.on_disableCrumbChk_clicked)
        self.ui.enableSupervisionTextChk.toggled.connect(self.on_enableSupervisionTextChk_clicked)
        self.ui.enableAirPlayChk.toggled.connect(self.on_enableAirPlayChk_clicked)

        ## INTERNAL OPTIONS PAGE ACTIONS
        self.ui.buildVersionChk.toggled.connect(self.on_buildVersionChk_clicked)
        self.ui.RTLChk.toggled.connect(self.on_RTLChk_clicked)
        self.ui.metalHUDChk.toggled.connect(self.on_metalHUDChk_clicked)
        self.ui.iMessageChk.toggled.connect(self.on_iMessageChk_clicked)
        self.ui.IDSChk.toggled.connect(self.on_IDSChk_clicked)
        self.ui.VCChk.toggled.connect(self.on_VCChk_clicked)
        self.ui.appStoreChk.toggled.connect(self.on_appStoreChk_clicked)
        self.ui.notesChk.toggled.connect(self.on_notesChk_clicked)
        self.ui.showTouchesChk.toggled.connect(self.on_showTouchesChk_clicked)
        self.ui.hideRespringChk.toggled.connect(self.on_hideRespringChk_clicked)
        self.ui.enableWakeVibrateChk.toggled.connect(self.on_enableWakeVibrateChk_clicked)
        self.ui.pasteSoundChk.toggled.connect(self.on_pasteSoundChk_clicked)
        self.ui.notifyPastesChk.toggled.connect(self.on_notifyPastesChk_clicked)

        ## DAEMONS PAGE ACTIONS
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

        ## POSTERBOARD PAGE ACTIONS
        self.ui.modifyPosterboardsChk.toggled.connect(self.on_modifyPosterboardsChk_clicked)
        self.ui.importTendiesBtn.clicked.connect(self.on_importTendiesBtn_clicked)
        self.ui.resetPRBExtBtn.clicked.connect(self.on_resetPRBExtBtn_clicked)
        self.ui.deleteAllDescriptorsBtn.clicked.connect(self.on_deleteAllDescriptorsBtn_clicked)
        self.ui.findPBBtn.clicked.connect(self.on_findPBBtn_clicked)
        self.ui.pbHelpBtn.clicked.connect(self.on_pbHelpBtn_clicked)

        ## RISKY OPTIONS PAGE ACTIONS
        self.ui.disableOTAChk.toggled.connect(self.on_disableOTAChk_clicked)
        self.ui.enableResolutionChk.toggled.connect(self.on_enableResolutionChk_clicked)
        self.ui.resHeightTxt.textEdited.connect(self.on_resHeightTxt_textEdited)
        self.ui.resWidthTxt.textEdited.connect(self.on_resWidthTxt_textEdited)

        ## APPLY PAGE ACTIONS
        self.ui.applyTweaksBtn.clicked.connect(self.on_applyPageBtn_clicked)
        self.ui.removeTweaksBtn.clicked.connect(self.on_removeTweaksBtn_clicked)
        self.ui.chooseGestaltBtn.clicked.connect(self.on_chooseGestaltBtn_clicked)
        self.ui.resetGestaltBtn.clicked.connect(self.on_resetGestaltBtn_clicked)

        ## SETTINGS PAGE ACTIONS
        self.ui.allowWifiApplyingChk.toggled.connect(self.on_allowWifiApplyingChk_toggled)
        self.ui.autoRebootChk.toggled.connect(self.on_autoRebootChk_toggled)
        self.ui.showRiskyChk.toggled.connect(self.on_showRiskyChk_toggled)
        # windows path fix toggle
        if os_name == "nt":
            self.ui.windowsPathFixChk.toggled.connect(self.on_windowsPathFixChk_toggled)
        else:
            self.ui.windowsPathFixChk.hide()
        self.ui.showAllSpoofableChk.toggled.connect(self.on_showAllSpoofableChk_toggled)

        self.ui.revertRdarChk.toggled.connect(self.on_revertRdarChk_toggled)

        self.ui.skipSetupChk.toggled.connect(self.on_skipSetupChk_toggled)
        self.ui.supervisionChk.toggled.connect(self.on_supervisionChk_toggled)
        self.ui.supervisionOrganization.textEdited.connect(self.on_supervisionOrgTxt_textEdited)
        self.ui.resetPairBtn.clicked.connect(self.on_resetPairBtn_clicked)

        ## MOBILE GESTALT PAGE ACTIONS
        self.ui.dynamicIslandDrp.activated.connect(self.on_dynamicIslandDrp_activated)
        self.ui.rdarFixChk.clicked.connect(self.on_rdarFixChk_clicked)
        self.ui.modelNameChk.toggled.connect(self.on_modelNameChk_clicked)
        self.ui.modelNameTxt.textEdited.connect(self.on_modelNameTxt_textEdited)

        self.ui.bootChimeChk.clicked.connect(self.on_bootChimeChk_clicked)
        self.ui.chargeLimitChk.clicked.connect(self.on_chargeLimitChk_clicked)
        self.ui.tapToWakeChk.clicked.connect(self.on_tapToWakeChk_clicked)
        self.ui.iphone16SettingsChk.clicked.connect(self.on_iphone16SettingsChk_clicked)
        self.ui.parallaxChk.clicked.connect(self.on_parallaxChk_clicked)
        self.ui.stageManagerChk.clicked.connect(self.on_stageManagerChk_clicked)
        self.ui.enableMedusaChk.clicked.connect(self.on_enableMedusaChk_clicked)
        self.ui.ipadAppsChk.clicked.connect(self.on_ipadAppsChk_clicked)
        self.ui.shutterChk.clicked.connect(self.on_shutterChk_clicked)
        self.ui.findMyFriendsChk.clicked.connect(self.on_findMyFriendsChk_clicked)
        self.ui.pencilChk.clicked.connect(self.on_pencilChk_clicked)
        self.ui.actionButtonChk.clicked.connect(self.on_actionButtonChk_clicked)

        self.ui.internalInstallChk.clicked.connect(self.on_internalInstallChk_clicked)
        self.ui.internalStorageChk.clicked.connect(self.on_internalStorageChk_clicked)
        self.ui.collisionSOSChk.clicked.connect(self.on_collisionSOSChk_clicked)
        self.ui.aodChk.clicked.connect(self.on_aodChk_clicked)
        self.ui.aodVibrancyChk.clicked.connect(self.on_aodVibrancyChk_clicked)

        self.ui.addGestaltKeyBtn.clicked.connect(self.on_addGestaltKeyBtn_clicked)
        self.ui.aiEnablerContent.hide()
        self.ui.resChangerContent.hide()
        self.ui.resHeightWarningLbl.hide()
        self.ui.resWidthWarningLbl.hide()
        self.ui.pbActionLbl.hide()


    ## GENERAL INTERFACE FUNCTIONS
    def updateInterfaceForNewDevice(self):
        # update the home page
        self.updatePhoneInfo()
    
    def updateAppVersionLabel(self):
        new_text: str = self.ui.appVersionLbl.text()
        new_text = new_text.replace("%VERSION", App_Version)
        if App_Build > 0:
            new_text = new_text.replace("%BETATAG", f"(beta {App_Build})")
        else:
            new_text = new_text.replace("%BETATAG", "")
        self.ui.appVersionLbl.setText(new_text)


    ## DEVICE BAR FUNCTIONS
    @QtCore.Slot()
    def refresh_devices(self):
        # get the devices
        self.device_manager.get_devices(self.settings)
        # clear the picker
        self.ui.devicePicker.clear()
        self.ui.restoreProgressBar.hide()
        if len(self.device_manager.devices) == 0:
            self.ui.devicePicker.setEnabled(False)
            self.ui.devicePicker.addItem('None')
            self.ui.pages.setCurrentIndex(Page.Home.value)
            self.ui.homePageBtn.setChecked(True)

            # hide all pages
            self.ui.sidebarDiv1.hide()

            self.ui.gestaltPageBtn.hide()
            self.ui.featureFlagsPageBtn.hide()
            self.ui.euEnablerPageBtn.hide()
            self.ui.springboardOptionsPageBtn.hide()
            self.ui.internalOptionsPageBtn.hide()
            self.ui.daemonsPageBtn.hide()
            self.ui.posterboardPageBtn.hide()
            self.ui.advancedPageBtn.hide()

            self.ui.sidebarDiv2.hide()
            self.ui.applyPageBtn.hide()

            self.ui.resetPairBtn.hide()
            self.ui.showRiskyChk.hide()
        else:
            self.ui.devicePicker.setEnabled(True)
            # populate the ComboBox with device names
            for device in self.device_manager.devices:
                tag = ""
                if self.device_manager.apply_over_wifi:
                    if device.connected_via_usb:
                        tag = " (@ USB)"
                    else:
                        tag = " (@ WiFi)"
                self.ui.devicePicker.addItem(f"{device.name}{tag}")
            
            # show all pages
            self.ui.sidebarDiv1.show()
            self.ui.springboardOptionsPageBtn.show()
            self.ui.internalOptionsPageBtn.show()
            self.ui.daemonsPageBtn.show()
            self.ui.posterboardPageBtn.show()

            if self.device_manager.allow_risky_tweaks:
                self.ui.advancedPageBtn.show()
                self.ui.resetPRBExtBtn.show()
            else:
                self.ui.advancedPageBtn.hide()
                self.ui.resetPRBExtBtn.hide()
            
            self.ui.sidebarDiv2.show()
            self.ui.applyPageBtn.show()

            self.ui.gestaltPageContent.setDisabled(False)
            self.ui.featureFlagsPageContent.setDisabled(False)
            self.ui.euEnablerPageContent.setDisabled(False)
            self.ui.springboardOptionsPageContent.setDisabled(False)
            self.ui.internalOptionsPageContent.setDisabled(False)
            self.ui.advancedOptionsPageContent.setDisabled(False)

            self.ui.resetPairBtn.show()
            self.ui.showRiskyChk.show()
        
        # update the selected device
        self.ui.devicePicker.setCurrentIndex(0)
        self.change_selected_device(0)

    def setup_spoofedModelDrp_models(self):
        # hide all the models first
        for i in range(1, self.ui.spoofedModelDrp.count()):
            try:
                self.ui.spoofedModelDrp.removeItem(1)
            except:
                pass
        # indexes 1-6 for iPhones, 7-(len(values) - 1) for iPads
        # TODO: Make this get fetched from the gui on app startup
        spoof_drp_options = ["iPhone 15 Pro (iPhone16,1)", "iPhone 15 Pro Max (iPhone16,2)", "iPhone 16 (iPhone17,3)", "iPhone 16 Plus (iPhone17,4)", "iPhone 16 Pro (iPhone17,1)", "iPhone 16 Pro Max (iPhone17,2)", "iPad Mini (A17 Pro) (W) (iPad16,1)", "iPad Mini (A17 Pro) (C) (iPad16,2)", "iPad Pro (13-inch) (M4) (W) (iPad16,5)", "iPad Pro (13-inch) (M4) (C) (iPad16,6)", "iPad Pro (11-inch) (M4) (W) (iPad16,3)", "iPad Pro (11-inch) (M4) (C) (iPad16,4)", "iPad Pro (12.9-inch) (M2) (W) (iPad14,5)", "iPad Pro (12.9-inch) (M2) (C) (iPad14,6)", "iPad Pro (11-inch) (M2) (W) (iPad14,3)", "iPad Pro (11-inch) (M2) (C) (iPad14,4)", "iPad Air (13-inch) (M2) (W) (iPad14,10)", "iPad Air (13-inch) (M2) (C) (iPad14,11)", "iPad Air (11-inch) (M2) (W) (iPad14,8)", "iPad Air (11-inch) (M2) (C) (iPad14,9)", "iPad Pro (11-inch) (M1) (W) (iPad13,4)", "iPad Pro (11-inch) (M1) (C) (iPad13,5)", "iPad Pro (12.9-inch) (M1) (W) (iPad13,8)", "iPad Pro (12.9-inch) (M1) (C) (iPad13,9)", "iPad Air (M1) (W) (iPad13,16)", "iPad Air (M1) (C) (iPad13,17)"]
        if self.device_manager.show_all_spoofable_models or self.device_manager.get_current_device_model().startswith("iPhone"):
            # re-enable iPhone spoof models
            self.ui.spoofedModelDrp.addItems(spoof_drp_options[:6])
        if self.device_manager.show_all_spoofable_models or self.device_manager.get_current_device_model().startswith("iPad"):
            # re-enable iPad spoof models
            self.ui.spoofedModelDrp.addItems(spoof_drp_options[6:])

    def change_selected_device(self, index):
        self.ui.showAllSpoofableChk.hide()
        if len(self.device_manager.devices) > 0:
            self.device_manager.set_current_device(index=index)
            # hide options that are for newer versions
            # remove the new dynamic island options
            MinTweakVersions = {
                "no_patch": [self.ui.chooseGestaltBtn, self.ui.gestaltPageBtn, self.ui.resetGestaltBtn, self.ui.gestaltLocationLbl, self.ui.gestaltLocationTitleLbl, self.ui.showAllSpoofableChk],
                "exploit": [("18.0", self.ui.featureFlagsPageBtn), ("18.1", self.ui.eligFileChk), ("1.0", self.ui.regularDomainsLbl)],
                "18.1": [self.ui.enableAIChk, self.ui.aiEnablerContent],
                "18.0": [self.ui.aodChk, self.ui.aodVibrancyChk, self.ui.iphone16SettingsChk]
            }
            MaxTweakVersions = {
                "patch": [self.ui.revertRdarChk, self.ui.revertRdarLine],
                "17.7": [self.ui.euEnablerContent],
                "18.0": [self.ui.photosChk, self.ui.aiChk]
            }

            try:
                self.ui.dynamicIslandDrp.removeItem(6)
                self.ui.dynamicIslandDrp.removeItem(5)
            except:
                pass
            self.set_rdar_fix_label()
            device_ver = Version(self.device_manager.data_singleton.current_device.version)
            patched: bool = self.device_manager.get_current_device_patched()
            # toggle option visibility for the minimum versions
            for version in MinTweakVersions.keys():
                if version == "exploit":
                    # disable if the exploit is not available
                    for pair in MinTweakVersions[version]:
                        if self.device_manager.data_singleton.current_device.has_exploit() and device_ver >= Version(pair[0]):
                            pair[1].show()
                        else:
                            pair[1].hide()
                elif version == "no_patch":
                    # hide patched version items
                    for view in MinTweakVersions[version]:
                        if patched:
                            view.hide()
                        else:
                            view.show()
                else:
                    # show views if the version is higher
                    parsed_ver = Version(version)
                    for view in MinTweakVersions[version]:
                        if device_ver >= parsed_ver:
                            view.show()
                        else:
                            view.hide()
            # toggle option visibility for the max versions
            for version in MaxTweakVersions.keys():
                if version == "patch":
                    if patched:
                        view.hide()
                    else:
                        view.show()
                else:
                    parsed_ver = Version(version)
                    for view in MaxTweakVersions[version]:
                        if device_ver <= parsed_ver:
                            view.show()
                        else:
                            view.hide()
            if device_ver >= Version("18.0"):
                # show the other dynamic island options
                self.ui.dynamicIslandDrp.addItem("2622 (iPhone 16 Pro Dynamic Island)")
                self.ui.dynamicIslandDrp.addItem("2868 (iPhone 16 Pro Max Dynamic Island)")
            # eligibility page button
            if not patched and device_ver >= Version("17.4") and (device_ver <= Version("17.7") or device_ver >= Version("18.1")):
                self.ui.euEnablerPageBtn.show()
            else:
                self.ui.euEnablerPageBtn.hide()
            
            # hide the ai content if not on
            if device_ver >= Version("18.1") and not tweaks["AIGestalt"].enabled:
                self.ui.aiEnablerContent.hide()
            self.setup_spoofedModelDrp_models()
        else:
            self.device_manager.set_current_device(index=None)

        # update the interface
        self.updateInterfaceForNewDevice()

    def loadSettings(self):
        self.settings = QtCore.QSettings()
        try:
            # load the settings
            apply_over_wifi = self.settings.value("apply_over_wifi", False, type=bool)
            auto_reboot = self.settings.value("auto_reboot", True, type=bool)
            risky_tweaks = self.settings.value("show_risky_tweaks", False, type=bool)
            show_all_spoofable = self.settings.value("show_all_spoofable_models", False, type=bool)
            skip_setup = self.settings.value("skip_setup", True, type=bool)
            supervised = self.settings.value("supervised", False, type=bool)
            organization_name = self.settings.value("organization_name", "", type=str)

            self.ui.allowWifiApplyingChk.setChecked(apply_over_wifi)
            self.ui.autoRebootChk.setChecked(auto_reboot)
            self.ui.showRiskyChk.setChecked(risky_tweaks)
            self.ui.showAllSpoofableChk.setChecked(show_all_spoofable)
            self.ui.skipSetupChk.setChecked(skip_setup)
            self.ui.supervisionChk.setChecked(supervised)
            self.ui.supervisionOrganization.setText(organization_name)

            # hide/show the warning label
            if skip_setup:
                self.ui.skipSetupOnLbl.show()
            else:
                self.ui.skipSetupOnLbl.hide()

            self.device_manager.apply_over_wifi = apply_over_wifi
            self.device_manager.auto_reboot = auto_reboot
            self.device_manager.allow_risky_tweaks = risky_tweaks
            self.device_manager.show_all_spoofable_models = show_all_spoofable
            self.device_manager.skip_setup = skip_setup
            self.device_manager.supervised = supervised
            self.device_manager.organization_name = organization_name
        except:
            pass
    

    ## SIDE BAR FUNCTIONS
    def on_homePageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.Home.value)
    
    def on_gestaltPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.Gestalt.value)

    def on_featureFlagsPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.FeatureFlags.value)
    
    def on_euEnablerPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.EUEnabler.value)

    def on_springboardOptionsPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.Springboard.value)

    def on_internalOptionsPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.InternalOptions.value)

    def on_daemonsPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.Daemons.value)

    def on_posterboardPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.Posterboard.value)

    def on_advancedPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.RiskyTweaks.value)

    def on_applyPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.Apply.value)

    def on_settingsPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.Settings.value)

    def update_side_btn_color(self, btn: QtWidgets.QToolButton, toggled: bool):
        if toggled:
            btn.setStyleSheet("QToolButton {\ncolor: #00FF00;\n}")
        else:
            btn.setStyleSheet("")
    

    ## HOME PAGE
    def updatePhoneInfo(self):
        # name label
        self.ui.phoneNameLbl.setText(self.device_manager.get_current_device_name())
        # version label
        ver = self.device_manager.get_current_device_version()
        build = self.device_manager.get_current_device_build()
        self.show_uuid = False
        if ver != "":
            self.show_version_text(version=ver, build=build)
        else:
            self.ui.phoneVersionLbl.setText("Please connect a device.")

    def toggle_version_label(self):
        if self.show_uuid:
            self.show_uuid = False
            ver = self.device_manager.get_current_device_version()
            build = self.device_manager.get_current_device_build()
            if ver != "":
                self.show_version_text(version=ver, build=build)
        else:
            self.show_uuid = True
            uuid = self.device_manager.get_current_device_uuid()
            if uuid != "":
                self.ui.phoneVersionLbl.setText(f"<a style=\"text-decoration:none; color: white\" href=\"#\">{uuid}</a>")

    def show_version_text(self, version: str, build: str):
        support_str: str = "<span style=\"color: #32d74b;\">Supported!</span></a>"
        if Version(version) < Version("17.0"):
            support_str = "<span style=\"color: #ff0000;\">Not Supported.</span></a>"
        elif self.device_manager.get_current_device_patched():
            # sparserestore fully patched
            support_str = "<span style=\"color: #ffff00;\">Partially Supported.</span></a>"
        self.ui.phoneVersionLbl.setText(f"<a style=\"text-decoration:none; color: white;\" href=\"#\">iOS {version} ({build}) {support_str}")

    ## HOME PAGE LINKS
    def on_bigMilkBtn_clicked(self):
        webbrowser.open_new_tab("https://cowabun.ga")

    def on_leminGitHubBtn_clicked(self):
        webbrowser.open_new_tab("https://github.com/leminlimez")
    def on_leminTwitterBtn_clicked(self):
        webbrowser.open_new_tab("https://twitter.com/LeminLimez")
    def on_leminKoFiBtn_clicked(self):
        webbrowser.open_new_tab("https://ko-fi.com/leminlimez")

    def on_posterRestoreBtn_clicked(self):
        webbrowser.open_new_tab("https://discord.gg/gWtzTVhMvh")
    def on_disfordottieBtn_clicked(self):
        webbrowser.open_new_tab("https://twitter.com/disfordottie")
    def on_mikasaBtn_clicked(self):
        webbrowser.open_new_tab("https://github.com/Mikasa-san/QuietDaemon")

    def on_libiBtn_clicked(self):
        webbrowser.open_new_tab("https://github.com/doronz88/pymobiledevice3")
    def on_jjtechBtn_clicked(self):
        webbrowser.open_new_tab("https://github.com/JJTech0130/TrollRestore")
    def on_qtBtn_clicked(self):
        webbrowser.open_new_tab("https://www.qt.io/product/development-tools")

    def on_discordBtn_clicked(self):
        webbrowser.open_new_tab("https://discord.gg/MN8JgqSAqT")
    def on_githubBtn_clicked(self):
        webbrowser.open_new_tab("https://github.com/leminlimez/Nugget")
    def on_bigNuggetBtn_clicked(self):
        webbrowser.open_new_tab("https://cowabun.ga")


    ## MOBILE GESTALT PAGE
    def set_rdar_fix_label(self):
        rdar_title = tweaks["RdarFix"].get_rdar_title()
        if rdar_title == "hide":
            self.ui.rdarFixChk.hide()
        else:
            self.ui.rdarFixChk.show()
            self.ui.rdarFixChk.setText(f"{rdar_title} (modifies resolution)")
    
    def on_dynamicIslandDrp_activated(self, index: int):
        if index == 0:
            tweaks["DynamicIsland"].set_enabled(False)
            tweaks["RdarFix"].set_di_type(-1)
        else:
            # disable X gestures on devices other than iPhone SEs
            # the lazy way, better option would be to remove it from the menu but I didn't want to rework all that
            model = self.device_manager.get_current_device_model()
            if index != 1 or (model == "iPhone12,8" or model == "iPhone14,6"):
                tweaks["DynamicIsland"].set_selected_option(index - 1)
            else:
                tweaks["DynamicIsland"].set_enabled(False)
            tweaks["RdarFix"].set_di_type(tweaks["DynamicIsland"].value[tweaks["DynamicIsland"].get_selected_option()])
        self.set_rdar_fix_label()
    def on_rdarFixChk_clicked(self, checked: bool):
        tweaks["RdarFix"].set_enabled(checked)

    def on_modelNameChk_clicked(self, checked: bool):
        tweaks["ModelName"].set_enabled(checked)
    def on_modelNameTxt_textEdited(self, text: str):
        tweaks["ModelName"].set_value(text, toggle_enabled=False)

    def on_bootChimeChk_clicked(self, checked: bool):
        tweaks["BootChime"].set_enabled(checked)
    def on_chargeLimitChk_clicked(self, checked: bool):
        tweaks["ChargeLimit"].set_enabled(checked)
    def on_tapToWakeChk_clicked(self, checked: bool):
        tweaks["TapToWake"].set_enabled(checked)
    def on_iphone16SettingsChk_clicked(self, checked: bool):
        tweaks["CameraButton"].set_enabled(checked)
    def on_parallaxChk_clicked(self, checked: bool):
        tweaks["Parallax"].set_enabled(checked)

    def on_stageManagerChk_clicked(self, checked: bool):
        tweaks["StageManager"].set_enabled(checked)
    def on_enableMedusaChk_clicked(self, checked: bool):
        tweaks["Medusa"].set_enabled(checked)
    def on_ipadAppsChk_clicked(self, checked: bool):
        tweaks["iPadApps"].set_enabled(checked)
    def on_shutterChk_clicked(self, checked: bool):
        # TODO: allow the user to select the region
        tweaks["Shutter"].set_enabled(checked)
    def on_findMyFriendsChk_clicked(self, checked: bool):
        tweaks["FindMyFriends"].set_enabled(checked)
    def on_pencilChk_clicked(self, checked: bool):
        tweaks["Pencil"].set_enabled(checked)
    def on_actionButtonChk_clicked(self, checked: bool):
        tweaks["ActionButton"].set_enabled(checked)

    def on_internalInstallChk_clicked(self, checked: bool):
        tweaks["InternalInstall"].set_enabled(checked)
    def on_internalStorageChk_clicked(self, checked: bool):
        tweaks["InternalStorage"].set_enabled(checked)

    def on_collisionSOSChk_clicked(self, checked: bool):
        tweaks["CollisionSOS"].set_enabled(checked)
    def on_aodChk_clicked(self, checked: bool):
        tweaks["AOD"].set_enabled(checked)
    def on_aodVibrancyChk_clicked(self, checked: bool):
        tweaks["AODVibrancy"].set_enabled(checked)

    def update_custom_gestalt_value_type(self, id, idx, valueField: QtWidgets.QLineEdit):
        new_str = CustomGestaltTweaks.set_tweak_value_type(id, idx)
        # update the value
        valueField.setText(new_str)

    def delete_custom_gestalt_key(self, id: int, widget: QtWidgets.QWidget):
        CustomGestaltTweaks.deactivate_tweak(id)
        self.ui.customKeysLayout.removeWidget(widget)
        widget.setParent(None)

    def on_addGestaltKeyBtn_clicked(self):
        # create a blank gestalt value with default value of 1
        key_identifier = CustomGestaltTweaks.create_tweak()

        widget = QtWidgets.QWidget()
        widget.setFixedHeight(35)
        widget.setStyleSheet("QWidget { background: none; border: 1px solid #3b3b3b; border-radius: 8px; }")
        hlayout = QtWidgets.QHBoxLayout(widget)
        hlayout.setContentsMargins(9, 2, 9, 2)

        # create the key field
        keyField = QtWidgets.QLineEdit(widget)
        # keyField.setMaximumWidth(200)
        keyField.setPlaceholderText("Key")
        keyField.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        keyField.setTextMargins(5, 0, 5, 0)
        keyField.textEdited.connect(lambda txt, id=key_identifier: CustomGestaltTweaks.set_tweak_key(id, txt))
        hlayout.addWidget(keyField)

        # create the delete button
        delBtn = QtWidgets.QToolButton(widget)
        delBtn.setIcon(QtGui.QIcon(":/icon/trash.svg"))
        delBtn.setStyleSheet("QToolButton { margin-right: 8px; background: none; border: none; }\nQToolButton:pressed { background: none; color: #FFFFFF; }")
        delBtn.clicked.connect(lambda _, id=key_identifier, w=widget: self.delete_custom_gestalt_key(id, w))
        hlayout.addWidget(delBtn)

        # create the type dropdown
        valueTypeDrp = QtWidgets.QComboBox(widget)
        valueTypeDrp.setStyleSheet("QComboBox {\n	background-color: #3b3b3b;\n    border: none;\n    color: #e8e8e8;\n    font-size: 14px;\n	padding-left: 8px;\n	border-radius: 8px;\n}\n\nQComboBox::drop-down {\n    image: url(:/icon/caret-down-fill.svg);\n	icon-size: 16px;\n    subcontrol-position: right center;\n	margin-right: 8px;\n}\n\nQComboBox QAbstractItemView {\n	background-color: #3b3b3b;\n    outline: none;\n	margin-top: 1px;\n}\n\nQComboBox QAbstractItemView::item {\n	background-color: #3b3b3b;\n	color: #e8e8e8;\n    padding-left: 8px;\n}\n\nQComboBox QAbstractItemView::item:hover {\n    background-color: #535353;\n    color: #ffffff;\n}")
        valueTypeDrp.setFixedWidth(120)
        valueTypeDrp.addItems(ValueTypeStrings)
        valueTypeDrp.setCurrentIndex(0)

        # create the value edit field
        valueField = QtWidgets.QLineEdit(widget)
        valueField.setMaximumWidth(175)
        valueField.setPlaceholderText("Value")
        valueField.setText("1")
        valueField.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        valueField.setTextMargins(5, 0, 5, 0)
        valueField.textEdited.connect(lambda txt, id=key_identifier: CustomGestaltTweaks.set_tweak_value(id, txt))

        valueTypeDrp.activated.connect(lambda idx, id=key_identifier, vf=valueField: self.update_custom_gestalt_value_type(id, idx, vf))
        hlayout.addWidget(valueTypeDrp)
        hlayout.addWidget(valueField)
        
        # add it to the main widget
        widget.setDisabled(False)
        self.ui.customKeysLayout.addWidget(widget)

    
    ## FEATURE FLAGS PAGE
    def on_clockAnimChk_toggled(self, checked: bool):
        tweaks["ClockAnim"].set_enabled(checked)
    def on_lockscreenChk_clicked(self, checked: bool):
        tweaks["Lockscreen"].set_enabled(checked)

    def on_photosChk_clicked(self, checked: bool):
        tweaks["PhotoUI"].set_enabled(checked)
    def on_aiChk_clicked(self, checked: bool):
        tweaks["AI"].set_enabled(checked)


    ## ELIGIBILITY PAGE
    def on_euEnablerEnabledChk_toggled(self, checked: bool):
        tweaks["EUEnabler"].set_enabled(checked)
    def on_methodChoiceDrp_activated(self, index: int):
        tweaks["EUEnabler"].set_selected_option(index)
    def on_regionCodeTxt_textEdited(self, text: str):
        tweaks["EUEnabler"].set_region_code(text)

    def on_enableAIChk_toggled(self, checked: bool):
        # tweaks["AIEligibility"].set_enabled(checked)
        tweaks["AIGestalt"].set_enabled(checked)
        # change the visibility of stuff
        if checked:
            self.ui.aiEnablerContent.show()
        else:
            self.ui.aiEnablerContent.hide()

    def on_eligFileChk_toggled(self, checked: bool):
        tweaks["AIEligibility"].set_enabled(checked)
        if checked:
            self.ui.languageTxt.show()
            self.ui.languageLbl.show()
        else:
            self.ui.languageTxt.hide()
            self.ui.languageLbl.hide()

    def on_languageTxt_textEdited(self, text: str):
        tweaks["AIEligibility"].set_language_code(text)
    
    def on_spoofedModelDrp_activated(self, index: int):
        idx_to_apply = index
        if not self.device_manager.show_all_spoofable_models and not self.device_manager.get_current_device_model().startswith("iPhone"):
            # offset the index for ipads
            idx_to_apply += 6
        tweaks["SpoofModel"].set_selected_option(idx_to_apply, is_enabled=(index != 0))
        tweaks["SpoofHardware"].set_selected_option(idx_to_apply, is_enabled=(index != 0 and self.ui.spoofHardwareChk.isChecked()))
        tweaks["SpoofCPU"].set_selected_option(idx_to_apply, is_enabled=(index != 0 and self.ui.spoofCPUChk.isChecked()))
    def on_spoofHardwareChk_toggled(self, checked: bool):
        tweaks["SpoofHardware"].set_enabled(checked and tweaks["SpoofHardware"].selected_option != 0)
    def on_spoofCPUChk_toggled(self, checked: bool):
        tweaks["SpoofCPU"].set_enabled(checked and tweaks["SpoofCPU"].selected_option != 0)


    ## SPRINGBOARD OPTIONS PAGE
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

    
    ## INTERNAL OPTIONS PAGE
    def on_buildVersionChk_clicked(self, checked: bool):
        tweaks["SBBuildNumber"].set_enabled(checked)
    def on_RTLChk_clicked(self, checked: bool):
        tweaks["RTL"].set_enabled(checked)
    def on_metalHUDChk_clicked(self, checked: bool):
        tweaks["MetalForceHudEnabled"].set_enabled(checked)
    def on_iMessageChk_clicked(self, checked: bool):
        tweaks["iMessageDiagnosticsEnabled"].set_enabled(checked)
    def on_IDSChk_clicked(self, checked: bool):
        tweaks["IDSDiagnosticsEnabled"].set_enabled(checked)
    def on_VCChk_clicked(self, checked: bool):
        tweaks["VCDiagnosticsEnabled"].set_enabled(checked)

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

    ## DAEMONS PAGE
    def on_modifyDaemonsChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_enabled(checked)
        self.ui.daemonsPageContent.setDisabled(not checked)

    def on_thermalmonitordChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.thermalmonitord.value, value=checked)
        if checked:
            # set the modify toggle checked so it actually applies
            self.on_modifyDaemonsChk_clicked(True)
    def on_otadChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.OTA.value, value=checked)
    def on_usageTrackingAgentChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.UsageTrackingAgent.value, value=checked)
    def on_gameCenterChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.GameCenter.value, value=checked)
    def on_screenTimeChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.ScreenTime.value, value=checked)
    def on_clearScreenTimeAgentChk_clicked(self, checked: bool):
        tweaks["ClearScreenTimeAgentPlist"].set_enabled(checked)
    def on_crashReportsChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.CrashReports.value, value=checked)
    def on_atwakeupChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.ATWAKEUP.value, value=checked)
    def on_tipsChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.Tips.value, value=checked)
    def on_vpndChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.VPN.value, value=checked)
    def on_wapicChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.ChineseLAN.value, value=checked)
    def on_healthdChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.HealthKit.value, value=checked)

    def on_airprintChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.AirPrint.value, value=checked)
    def on_assistiveTouchChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.AssistiveTouch.value, value=checked)
    def on_icloudChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.iCloud.value, value=checked)
    def on_hotspotChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.InternetTethering.value, value=checked)
    def on_passbookChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.PassBook.value, value=checked)
    def on_spotlightChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.Spotlight.value, value=checked)
    def on_voiceControlChk_clicked(self, checked: bool):
        tweaks["Daemons"].set_multiple_values(Daemon.VoiceControl.value, value=checked)

    ## PosterBoard Page
    def delete_pb_file(self, file, widget):
        if file in tweaks["PosterBoard"].tendies:
            tweaks["PosterBoard"].tendies.remove(file)
        widget.deleteLater()

    def load_posterboard(self):
        if len(tweaks["PosterBoard"].tendies) == 0:
            return
        
        if self.pb_mainLayout == None:
            # Create scroll layout
            self.pb_mainLayout = QtWidgets.QVBoxLayout()
            self.pb_mainLayout.setContentsMargins(0, 0, 0, 0)
            self.pb_mainLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
            # Create a QWidget to act as the container for the scroll area
            scrollWidget = QtWidgets.QWidget()

            # Set the main layout (containing all the widgets) on the scroll widget
            scrollWidget.setLayout(self.pb_mainLayout)

            # Create a QScrollArea to hold the content widget (scrollWidget)
            scrollArea = QtWidgets.QScrollArea()
            scrollArea.setWidgetResizable(True)  # Allow the content widget to resize within the scroll area
            scrollArea.setFrameStyle(QtWidgets.QScrollArea.NoFrame)  # Remove the outline from the scroll area

            # Set the scrollWidget as the content widget of the scroll area
            scrollArea.setWidget(scrollWidget)

            # Set the size policy of the scroll area to expand in both directions
            scrollArea.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

            # Set the scroll area as the central widget of the main window
            scrollLayout = QtWidgets.QVBoxLayout()
            scrollLayout.setContentsMargins(0, 0, 0, 0)
            scrollLayout.addWidget(scrollArea)
            self.ui.pbFilesList.setLayout(scrollLayout)

        widgets = {}
        # Iterate through the files
        for tendie in tweaks["PosterBoard"].tendies:
            if tendie.loaded:
                continue
            widget = QtWidgets.QWidget()
            widgets[tendie] = widget

            # create the icon/label
            titleBtn = QtWidgets.QToolButton(widget)
            titleBtn.setIcon(QtGui.QIcon(tendie.get_icon()))
            titleBtn.setIconSize(QtCore.QSize(20, 20))
            titleBtn.setText(f"   {tendie.name}")
            titleBtn.setStyleSheet("QToolButton {\n    background-color: transparent;\n	icon-size: 20px;\n}")
            titleBtn.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            titleBtn.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

            delBtn = QtWidgets.QToolButton(widget)
            delBtn.setIcon(QtGui.QIcon(":/icon/trash.svg"))
            delBtn.clicked.connect(lambda _, file=tendie: (widgets[file].deleteLater(), tweaks["PosterBoard"].tendies.remove(file)))

            spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            # main layout
            layout = QtWidgets.QHBoxLayout(widget)
            layout.setContentsMargins(0, 0, 0, 9)
            layout.addWidget(titleBtn)
            layout.addItem(spacer)
            layout.addWidget(delBtn)
            # Add the widget to the mainLayout
            widget.setLayout(layout)
            self.pb_mainLayout.addWidget(widget)
            tendie.loaded = True

    def on_modifyPosterboardsChk_clicked(self, checked: bool):
        tweaks["PosterBoard"].set_enabled(checked)
        self.ui.posterboardPageContent.setDisabled(not checked)
    def on_importTendiesBtn_clicked(self):
        selected_files, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Select PosterBoard Files", "", "Zip Files (*.tendies)", options=QtWidgets.QFileDialog.ReadOnly)
        tweaks["PosterBoard"].resetting = False
        self.ui.pbActionLbl.hide()
        if selected_files != None and len(selected_files) > 0:
            # user selected files, add them
            for file in selected_files:
                if not tweaks["PosterBoard"].add_tendie(file):
                    # alert that there are too many
                    detailsBox = QtWidgets.QMessageBox()
                    detailsBox.setIcon(QtWidgets.QMessageBox.Critical)
                    detailsBox.setWindowTitle("Error!")
                    detailsBox.setText("You selected too many descriptors! The limit is 10.")
                    detailsBox.exec()
            self.load_posterboard()

    def on_deleteAllDescriptorsBtn_clicked(self):
        if tweaks["PosterBoard"].resetting and tweaks["PosterBoard"].resetType == 0:
            tweaks["PosterBoard"].resetting = False
            self.ui.pbActionLbl.hide()
        else:
            tweaks["PosterBoard"].resetting = True
            tweaks["PosterBoard"].resetType = 0
            self.ui.pbActionLbl.setText("! Clearing Collections Wallpapers")
            self.ui.pbActionLbl.show()
    def on_resetPRBExtBtn_clicked(self):
        if tweaks["PosterBoard"].resetting and tweaks["PosterBoard"].resetType == 1:
            tweaks["PosterBoard"].resetting = False
            self.ui.pbActionLbl.hide()
        else:
            tweaks["PosterBoard"].resetting = True
            tweaks["PosterBoard"].resetType = 1
            self.ui.pbActionLbl.setText("! Resetting PRB Extension")
            self.ui.pbActionLbl.show()

    def on_findPBBtn_clicked(self):
        webbrowser.open_new_tab("https://cowabun.ga/wallpapers")

    def on_pbHelpBtn_clicked(self):
        dialog = PBHelpDialog()
        dialog.exec()


    ## Risky Options Page
    def on_disableOTAChk_clicked(self, checked: bool):
        tweaks["DisableOTAFile"].set_enabled(checked)

    def on_enableResolutionChk_clicked(self, checked: bool):
        tweaks["CustomResolution"].set_enabled(checked)
        # toggle the ui content
        if checked:
            self.ui.resChangerContent.show()
        else:
            self.ui.resChangerContent.hide()
    def on_resHeightTxt_textEdited(self, txt: str):
        if txt == "":
            # remove the canvas_height value
            tweaks["CustomResolution"].value.pop("canvas_height", None)
            self.ui.resHeightWarningLbl.hide()
            return
        try:
            val = int(txt)
            tweaks["CustomResolution"].value["canvas_height"] = val
            self.ui.resHeightWarningLbl.hide()
        except:
            self.ui.resHeightWarningLbl.show()
    def on_resWidthTxt_textEdited(self, txt: str):
        if txt == "":
            # remove the canvas_width value
            tweaks["CustomResolution"].value.pop("canvas_width", None)
            self.ui.resWidthWarningLbl.hide()
            return
        try:
            val = int(txt)
            tweaks["CustomResolution"].value["canvas_width"] = val
            self.ui.resWidthWarningLbl.hide()
        except:
            self.ui.resWidthWarningLbl.show()

    
    ## SETTINGS PAGE
    def on_allowWifiApplyingChk_toggled(self, checked: bool):
        self.device_manager.apply_over_wifi = checked
        # save the setting
        self.settings.setValue("apply_over_wifi", checked)
    def on_showRiskyChk_toggled(self, checked: bool):
        self.device_manager.allow_risky_tweaks = checked
        # save the setting
        self.settings.setValue("show_risky_tweaks", checked)
        # toggle the button visibility
        if checked:
            self.ui.advancedPageBtn.show()
            self.ui.resetPRBExtBtn.show()
        else:
            self.ui.advancedPageBtn.hide()
            self.ui.resetPRBExtBtn.hide()
    def on_windowsPathFixChk_toggled(self, checked: bool):
        self.device_manager.windows_path_fix = checked
        # save the setting
        self.settings.setValue("windows_path_fix", checked)
    def on_showAllSpoofableChk_toggled(self, checked: bool):
        self.device_manager.show_all_spoofable_models = checked
        # save the setting
        self.settings.setValue("show_all_spoofable_models", checked)
        # refresh the list of spoofable models
        self.setup_spoofedModelDrp_models()
    def on_autoRebootChk_toggled(self, checked: bool):
        self.device_manager.auto_reboot = checked
        # save the setting
        self.settings.setValue("auto_reboot", checked)

    def on_revertRdarChk_toggled(self, checked: bool):
        tweaks["RdarFix"].set_enabled(checked)

    def on_skipSetupChk_toggled(self, checked: bool):
        self.device_manager.skip_setup = checked
        # save the setting
        self.settings.setValue("skip_setup", checked)
        # hide/show the warning label
        if checked:
            self.ui.skipSetupOnLbl.show()
        else:
            self.ui.skipSetupOnLbl.hide()
    def on_supervisionOrgTxt_textEdited(self, text: str):
        self.device_manager.organization_name = text
        self.settings.setValue("organization_name", text)
    def on_supervisionChk_toggled(self, checked: bool):
        self.device_manager.supervised = checked
        # save the setting
        self.settings.setValue("supervised", checked)

    # Device Options
    def on_resetPairBtn_clicked(self):
        self.device_manager.reset_device_pairing()


    ## APPLY PAGE
    def on_chooseGestaltBtn_clicked(self):
        selected_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Mobile Gestalt File", "", "Plist Files (*.plist)", options=QtWidgets.QFileDialog.ReadOnly)
        if selected_file == "" or selected_file == None:
            self.device_manager.data_singleton.gestalt_path = None
            self.ui.gestaltLocationLbl.setText("None")
            # show the warning labels
            self.ui.mgaWarningLbl.show()
            self.ui.mgaWarningLbl2.show()
        else:
            # verify that the gestalt is correct and compatible
            with open(selected_file, 'rb') as in_fp:
                gestalt_plist = plistlib.load(in_fp)
            if not "CacheExtra" in gestalt_plist:
                detailsBox = QtWidgets.QMessageBox()
                detailsBox.setIcon(QtWidgets.QMessageBox.Critical)
                detailsBox.setWindowTitle("Error!")
                detailsBox.setText("The file is not a mobile gestalt file!")
                detailsBox.exec()
                return
            if (
                not "qNNddlUK+B/YlooNoymwgA" in gestalt_plist["CacheExtra"]
                or not "0+nc/Udy4WNG8S+Q7a/s1A" in gestalt_plist["CacheExtra"]
                or gestalt_plist["CacheExtra"]["qNNddlUK+B/YlooNoymwgA"] != self.device_manager.data_singleton.current_device.version
                or gestalt_plist["CacheExtra"]["0+nc/Udy4WNG8S+Q7a/s1A"] != self.device_manager.data_singleton.current_device.model
            ):
                dialog = GestaltDialog(
                        device_manager=self.device_manager,
                        gestalt_label=self.ui.gestaltLocationLbl,
                        selected_file=selected_file
                    )
                dialog.exec()
            else:
                self.device_manager.data_singleton.gestalt_path = selected_file
                self.ui.gestaltLocationLbl.setText(selected_file)
            # hide the warning labels
            self.ui.mgaWarningLbl.hide()
            self.ui.mgaWarningLbl2.hide()

    def update_label(self, txt: str):
        self.ui.statusLbl.setText(txt)
    def update_bar(self, percent):
        self.ui.restoreProgressBar.setValue(int(percent))
    def on_removeTweaksBtn_clicked(self):
        # TODO: Add threading here
        self.device_manager.apply_changes(resetting=True, update_label=self.update_label)
    def on_resetGestaltBtn_clicked(self):
        self.device_manager.reset_mobilegestalt(self.settings, update_label=self.update_label)

    @QtCore.Slot()
    def on_applyTweaksBtn_clicked(self):
        # TODO: Add threading here
        self.device_manager.apply_changes(update_label=self.update_label)
