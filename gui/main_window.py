from PySide6 import QtCore, QtWidgets, QtGui
from enum import Enum
from os import name as os_name
import webbrowser
import plistlib

from pymobiledevice3.lockdown import create_using_usbmux

from qt.ui_mainwindow import Ui_Nugget
import gui.pages as Pages

from controllers.web_request_handler import is_update_available

from devicemanagement.constants import Version
from devicemanagement.device_manager import DeviceManager

from gui.dialogs import GestaltDialog, UpdateAppDialog
from gui.apply_worker import ApplyThread, ApplyAlertMessage

from tweaks.tweaks import tweaks

App_Version = "5.2"
App_Build = 3

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
        self.thread_in_progress = False
        self.threadpool = QtCore.QThreadPool()
        self.loadSettings()

        # pre-load the pages
        self.pages = {
            Page.Posterboard: Pages.Posterboard(window=self, ui=self.ui),
            Page.Gestalt: Pages.MobileGestalt(window=self, ui=self.ui),
            Page.EUEnabler: Pages.Eligibility(window=self, ui=self.ui),
            Page.FeatureFlags: Pages.FeatureFlags(ui=self.ui),
            Page.Springboard: Pages.Springboard(ui=self.ui),
            Page.InternalOptions: Pages.Internal(ui=self.ui),
            Page.Daemons: Pages.Daemons(ui=self.ui),
            Page.RiskyTweaks: Pages.Risky(ui=self.ui),
            Page.Settings: Pages.Settings(window=self, ui=self.ui)
        }

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
        self.ui.snoolieBtn.clicked.connect(self.on_snoolieBtn_clicked)
        self.ui.disfordottieBtn.clicked.connect(self.on_disfordottieBtn_clicked)
        self.ui.mikasaBtn.clicked.connect(self.on_mikasaBtn_clicked)

        self.ui.libiBtn.clicked.connect(self.on_libiBtn_clicked)
        self.ui.jjtechBtn.clicked.connect(self.on_jjtechBtn_clicked)
        self.ui.qtBtn.clicked.connect(self.on_qtBtn_clicked)

        self.ui.discordBtn.clicked.connect(self.on_discordBtn_clicked)

        ## APPLY PAGE ACTIONS
        self.ui.applyTweaksBtn.clicked.connect(self.on_applyPageBtn_clicked)
        self.ui.removeTweaksBtn.clicked.connect(self.on_removeTweaksBtn_clicked)
        self.ui.chooseGestaltBtn.clicked.connect(self.on_chooseGestaltBtn_clicked)
        self.ui.resetGestaltBtn.clicked.connect(self.on_resetGestaltBtn_clicked)

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
            if device_ver < Version("18.2"):
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
        self.pages[Page.Gestalt].load()
        self.ui.pages.setCurrentIndex(Page.Gestalt.value)

    def on_featureFlagsPageBtn_clicked(self):
        self.pages[Page.FeatureFlags].load()
        self.ui.pages.setCurrentIndex(Page.FeatureFlags.value)
    
    def on_euEnablerPageBtn_clicked(self):
        self.pages[Page.EUEnabler].load()
        self.ui.pages.setCurrentIndex(Page.EUEnabler.value)

    def on_springboardOptionsPageBtn_clicked(self):
        self.pages[Page.Springboard].load()
        self.ui.pages.setCurrentIndex(Page.Springboard.value)

    def on_internalOptionsPageBtn_clicked(self):
        self.pages[Page.InternalOptions].load()
        self.ui.pages.setCurrentIndex(Page.InternalOptions.value)

    def on_daemonsPageBtn_clicked(self):
        self.pages[Page.Daemons].load()
        self.ui.pages.setCurrentIndex(Page.Daemons.value)

    def on_posterboardPageBtn_clicked(self):
        self.pages[Page.Posterboard].load()
        self.ui.pages.setCurrentIndex(Page.Posterboard.value)

    def on_advancedPageBtn_clicked(self):
        self.pages[Page.RiskyTweaks].load()
        self.ui.pages.setCurrentIndex(Page.RiskyTweaks.value)

    def on_applyPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.Apply.value)

    def on_settingsPageBtn_clicked(self):
        self.pages[Page.Settings].load()
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
    def on_snoolieBtn_clicked(self):
        webbrowser.open_new_tab("https://github.com/0xilis/python-aar-stuff")
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
        self.apply_changes(resetting=True)
    def on_resetGestaltBtn_clicked(self):
        self.device_manager.reset_mobilegestalt(self.settings, update_label=self.update_label)

    @QtCore.Slot()
    def on_applyTweaksBtn_clicked(self):
        self.apply_changes()

    def apply_changes(self, resetting: bool = False):
        if not self.thread_in_progress:
            self.thread_in_progress = True
            self.toggle_thread_btns(disabled=True)
            self.worker_thread = ApplyThread(manager=self.device_manager, resetting=resetting)
            self.worker_thread.progress.connect(self.ui.statusLbl.setText)
            self.worker_thread.alert.connect(self.alert_message)
            self.worker_thread.finished.connect(self.finish_apply_thread)
            self.worker_thread.finished.connect(self.worker_thread.deleteLater)
            self.worker_thread.start()
    def alert_message(self, alert: ApplyAlertMessage):
        print(alert.txt)
        detailsBox = QtWidgets.QMessageBox()
        detailsBox.setIcon(alert.icon)
        detailsBox.setWindowTitle(alert.title)
        detailsBox.setText(alert.txt)
        if alert.detailed_txt != None:
            detailsBox.setDetailedText(alert.detailed_txt)
        detailsBox.exec()

    def finish_thread(self):
        self.thread_in_progress = False
        self.toggle_thread_btns(disabled=False)
    def toggle_thread_btns(self, disabled: bool):
        self.ui.applyTweaksBtn.setDisabled(disabled)
        self.ui.resetGestaltBtn.setDisabled(disabled)
        self.ui.removeTweaksBtn.setDisabled(disabled)
