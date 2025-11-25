from PySide6 import QtCore, QtWidgets
import plistlib

from qt.ui_mainwindow import Ui_Nugget
import gui.pages as Pages

from controllers.web_request_handler import is_update_available
from controllers.translator import Translator
import controllers.video_handler as video_handler

from devicemanagement.constants import Version
from devicemanagement.device_manager import DeviceManager

from gui.dialogs import GestaltDialog, UpdateAppDialog
from gui.pages.reset_dialog import ResetDialog
from gui.apply_worker import ApplyThread, ApplyAlertMessage, RefreshDevicesThread, set_sudo_pwd, set_sudo_complete, get_sudo_pwd
from gui.pages.pages_list import Page
from restore.bookrestore import BookRestoreFileTransferMethod

from tweaks.tweaks import tweaks, TweakID

App_Version = "7.0"
App_Build = 12

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, device_manager: DeviceManager, translator: Translator):
        super(MainWindow, self).__init__()
        self.device_manager = device_manager
        self.translator = translator
        self.settings = self.translator.settings
        self.ui = Ui_Nugget()
        self.ui.setupUi(self)
        self.noneText = self.tr("None")
        self.apply_in_progress = False
        self.refresh_in_progress = False
        self.threadpool = QtCore.QThreadPool()
        self.loadSettings()
        self.initial_load = True

        # hide every page
        self.ui.posterboardPageBtn.hide()
        self.ui.templatePageBtn.hide()
        self.ui.gestaltPageBtn.hide()
        self.ui.euEnablerPageBtn.hide()
        self.ui.featureFlagsPageBtn.hide()
        self.ui.statusBarPageBtn.hide()
        self.ui.springboardOptionsPageBtn.hide()
        self.ui.internalOptionsPageBtn.hide()
        self.ui.daemonsPageBtn.hide()
        self.ui.templatesPageBtn.hide()
        self.ui.advancedPageBtn.hide()
        self.ui.miscOptionsBtn.hide()
        self.ui.applyPageBtn.hide()
        self.ui.sidebarDiv1.hide()
        self.ui.sidebarDiv2.hide()

        # pre-load the pages
        self.pages = {
            Page.Home: Pages.Home(window=self, ui=self.ui),
            Page.Posterboard: Pages.Posterboard(window=self, ui=self.ui),
            Page.Gestalt: Pages.MobileGestalt(window=self, ui=self.ui),
            Page.EUEnabler: Pages.Eligibility(window=self, ui=self.ui),
            Page.FeatureFlags: Pages.FeatureFlags(ui=self.ui),
            Page.StatusBar: Pages.StatusBar(ui=self.ui),
            Page.Springboard: Pages.Springboard(ui=self.ui),
            Page.InternalOptions: Pages.Internal(ui=self.ui),
            Page.Daemons: Pages.Daemons(ui=self.ui),
            Page.Templates: Pages.Templates(window=self, ui=self.ui),
            Page.RiskyTweaks: Pages.Risky(ui=self.ui),
            Page.Settings: Pages.Settings(window=self, ui=self.ui)
        }

        # Check for an update
        if is_update_available(App_Version, App_Build):
            # notify with prompt to download the new version from github
            UpdateAppDialog().exec()
        # Update the app version/build number label
        self.updateAppVersionLabel()
        self.pages[Page.Home].load()

        ## DEVICE BAR
        self.refresh_devices()

        self.ui.refreshBtn.clicked.connect(self.refresh_devices)
        self.ui.devicePicker.currentIndexChanged.connect(self.change_selected_device)

        ## SIDE BAR ACTIONS
        self.ui.homePageBtn.clicked.connect(self.on_homePageBtn_clicked)
        self.ui.gestaltPageBtn.clicked.connect(self.on_gestaltPageBtn_clicked)
        self.ui.featureFlagsPageBtn.clicked.connect(self.on_featureFlagsPageBtn_clicked)
        self.ui.euEnablerPageBtn.clicked.connect(self.on_euEnablerPageBtn_clicked)
        self.ui.statusBarPageBtn.clicked.connect(self.on_statusBarPageBtn_clicked)
        self.ui.springboardOptionsPageBtn.clicked.connect(self.on_springboardOptionsPageBtn_clicked)
        self.ui.internalOptionsPageBtn.clicked.connect(self.on_internalOptionsPageBtn_clicked)
        self.ui.daemonsPageBtn.clicked.connect(self.on_daemonsPageBtn_clicked)
        self.ui.posterboardPageBtn.clicked.connect(self.on_posterboardPageBtn_clicked)
        self.ui.templatesPageBtn.clicked.connect(self.on_templatesPageBtn_clicked)
        self.ui.advancedPageBtn.clicked.connect(self.on_advancedPageBtn_clicked)
        self.ui.miscOptionsBtn.clicked.connect(self.on_miscOptionsBtn_clicked)
        self.ui.applyPageBtn.clicked.connect(self.on_applyPageBtn_clicked)
        self.ui.settingsPageBtn.clicked.connect(self.on_settingsPageBtn_clicked)

        ## APPLY PAGE ACTIONS
        self.ui.applyTweaksBtn.clicked.connect(self.on_applyPageBtn_clicked)
        self.ui.removeTweaksBtn.clicked.connect(self.on_removeTweaksBtn_clicked)
        self.ui.chooseGestaltBtn.clicked.connect(self.on_chooseGestaltBtn_clicked)


    ## GENERAL INTERFACE FUNCTIONS
    def updateInterfaceForNewDevice(self):
        # update the home page
        self.pages[Page.Home].updatePhoneInfo()
    
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
        if not self.refresh_in_progress:
            self.refresh_in_progress = True
            self.ui.refreshBtn.setDisabled(True)
            self.refresh_worker_thread = RefreshDevicesThread(manager=self.device_manager, settings=self.settings)
            self.refresh_worker_thread.alert.connect(self.alert_message)
            self.refresh_worker_thread.finished.connect(self.refresh_devices_finished)
            self.refresh_worker_thread.finished.connect(self.refresh_worker_thread.deleteLater)
            self.refresh_worker_thread.start()

    def warn_for_dev_beta(self):
        ver = self.device_manager.get_current_device_version()
        if ver == "":
            return
        if Version(ver) > Version("26.0") and not self.device_manager.get_current_device_build()[-1].isdigit():
            self.alert_message(ApplyAlertMessage(
                txt=self.tr("Warning: You are on iOS 26 beta.\n\nThis has been known to cause problems and potentially lead to bootloops.\n\nUse at your own risk!"),
                title="Warning", icon=QtWidgets.QMessageBox.Warning
            ), log_to_console=False)

    def refresh_devices_finished(self):
        self.refresh_in_progress = False
        self.toggle_thread_btns(disabled=False)
        # clear the picker
        self.ui.devicePicker.clear()
        self.ui.restoreProgressBar.hide()
        if len(self.device_manager.devices) == 0:
            self.ui.devicePicker.setEnabled(False)
            self.ui.devicePicker.addItem(self.noneText)
            self.ui.pages.setCurrentIndex(Page.Home.value)
            self.ui.homePageBtn.setChecked(True)

            # hide all pages
            self.ui.sidebarDiv1.hide()

            self.ui.gestaltPageBtn.hide()
            self.ui.featureFlagsPageBtn.hide()
            self.ui.euEnablerPageBtn.hide()
            self.ui.statusBarPageBtn.hide()
            self.ui.springboardOptionsPageBtn.hide()
            self.ui.internalOptionsPageBtn.hide()
            self.ui.daemonsPageBtn.hide()
            self.ui.templatesPageBtn.hide()
            self.ui.posterboardPageBtn.hide()
            self.ui.advancedPageBtn.hide()
            self.ui.miscOptionsBtn.hide()

            self.ui.sidebarDiv2.hide()
            self.ui.applyPageBtn.hide()

            self.ui.resetPairBtn.hide()
            self.ui.pocketPosterHelperBtn.hide()
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
            self.ui.statusBarPageBtn.show()
            self.ui.springboardOptionsPageBtn.show()
            self.ui.internalOptionsPageBtn.show()
            self.ui.daemonsPageBtn.show()
            self.ui.templatesPageBtn.show()
            self.ui.posterboardPageBtn.show()
            self.ui.miscOptionsBtn.show()

            if self.device_manager.allow_risky_tweaks:
                try:
                    self.ui.resetPBDrp.removeItem(4)
                except:
                    pass
                self.ui.resetPBDrp.addItem("PB Extensions", "PB Extensions")
            else:
                self.ui.advancedPageBtn.hide()
                try:
                    self.ui.resetPBDrp.removeItem(4)
                except:
                    pass
            
            self.ui.sidebarDiv2.show()
            self.ui.applyPageBtn.show()

            self.ui.gestaltPageContent.setDisabled(False)
            self.ui.featureFlagsPageContent.setDisabled(False)
            self.ui.euEnablerPageContent.setDisabled(False)
            self.ui.springboardOptionsPageContent.setDisabled(False)
            self.ui.internalOptionsPageContent.setDisabled(False)
            self.ui.advancedOptionsPageContent.setDisabled(False)
            self.ui.pbPages.setDisabled(False)

            self.ui.resetPairBtn.show()
            self.ui.pocketPosterHelperBtn.show()
            self.ui.showRiskyChk.show()
        
        # update the selected device
        self.ui.devicePicker.setCurrentIndex(0)

    def change_selected_device(self, index):
        self.ui.showAllSpoofableChk.hide()
        if len(self.device_manager.devices) > 0:
            self.device_manager.set_current_device(index=index)
            # hide options that are for newer versions
            # remove the new dynamic island options
            MinTweakVersions = {
                "no_patch": [self.ui.chooseGestaltBtn, self.ui.gestaltPageBtn, self.ui.gestaltLocationLbl, self.ui.gestaltLocationTitleLbl, self.ui.showAllSpoofableChk],
                "exploit": [("18.0", self.ui.featureFlagsPageBtn), ("18.1", self.ui.eligFileChk), ("1.0", self.ui.regularDomainsLbl)],
                "18.1": [self.ui.enableAIChk, self.ui.aiEnablerContent],
                "18.0": [self.ui.aodChk, self.ui.aodVibrancyChk, self.ui.iphone16SettingsChk],
                "26.0": [self.ui.liquidGlassOptionsContent]
            }
            MaxTweakVersions = {
                "17.7": [self.ui.euEnablerContent],
                "18.0": [self.ui.photosChk, self.ui.aiChk],
                "19.0": [self.ui.resChangerContent, self.ui.metalHUDContent]
            }

            try:
                self.ui.dynamicIslandDrp.removeItem(6)
                self.ui.dynamicIslandDrp.removeItem(5)
                self.ui.dynamicIslandDrp.removeItem(5)
            except:
                pass
            if TweakID.RdarFix in tweaks:
                self.pages[Page.Gestalt].set_rdar_fix_label()
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
                if device_ver >= Version("26.0"):
                    self.ui.dynamicIslandDrp.addItem("2736 (iPhone Air Dynamic Island)")
            # eligibility page button
            if not patched and device_ver >= Version("17.4") and (device_ver <= Version("17.7") or device_ver >= Version("18.1")):
                self.ui.euEnablerPageBtn.show()
            else:
                self.ui.euEnablerPageBtn.hide()

            # hide risky/advanced page on iOS 26
            if self.device_manager.allow_risky_tweaks and device_ver < Version("19.0"):
                self.ui.advancedPageBtn.show()
            else:
                self.ui.advancedPageBtn.hide()
            # toggle AtWakeUp checkbox with risky tweaks
            self.ui.atwakeupChk.setVisible(self.device_manager.allow_risky_tweaks)
            
            # hide the ai content if not on
            if device_ver >= Version("18.1") and (not TweakID.AIGestalt in tweaks or not tweaks[TweakID.AIGestalt].enabled):
                self.ui.aiEnablerContent.hide()
            if device_ver < Version("18.2"):
                self.pages[Page.Gestalt].setup_spoofedModelDrp_models()

            # hide posterboard .aar video option on ipads
            is_iphone = self.device_manager.get_current_device_model().startswith("iPhone")
            if not is_iphone:
                # force looping
                tweaks[TweakID.PosterBoard].loop_video = True
            is_looping = tweaks[TweakID.PosterBoard].loop_video
            self.ui.pbVideoThumbLbl.setVisible(is_iphone and not is_looping)
            self.ui.chooseThumbBtn.setVisible(is_iphone and not is_looping)
            self.ui.caVideoChk.setVisible(is_iphone)
            self.ui.exportPBVideoBtn.setVisible(is_looping and tweaks[TweakID.PosterBoard].videoFile != None)
            # show status bar date on ipads
            self.ui.dateChk.setVisible(not is_iphone)
            self.ui.dateTxt.setVisible(not is_iphone)
            # show floating tab bar on ipads and keyflicks on phones
            self.ui.floatingTabBarContent.setVisible(not is_iphone)
            self.ui.keyFlickContent.setVisible(is_iphone and device_ver < Version("26.1"))
            # iPadOS stuff
            self.ui.enableiPadOSChk.setVisible(is_iphone)
            self.ui.stageManagerChk.setVisible(not is_iphone)

            # bookrestore stuff
            if self.device_manager.data_singleton.current_device.has_bookrestore():
                self.ui.bookrestoreWidget.show()
                self.ui.booksContainerUUIDTxt.setText(self.device_manager.data_singleton.current_device.books_container_uuid)
            else:
                self.ui.bookrestoreWidget.hide()

            # show the PB if initial load is true
            if self.initial_load:
                self.initial_load = False
                if len(tweaks[TweakID.PosterBoard].tendies) > 0:
                    self.pages[Page.Posterboard].load()
                    self.ui.pages.setCurrentIndex(Page.Posterboard.value)
                    self.ui.posterboardPageBtn.setChecked(True)
                    self.ui.homePageBtn.setChecked(False)
                elif len(tweaks[TweakID.Templates].templates) > 0:
                    self.pages[Page.Templates].load()
                    self.ui.pages.setCurrentIndex(Page.Templates.value)
                    self.ui.templatePageBtn.setChecked(True)
                    self.ui.homePageBtn.setChecked(False)
        else:
            self.device_manager.set_current_device(index=None)

        # update the interface
        self.updateInterfaceForNewDevice()
        if index > -1:
            self.warn_for_dev_beta()

    def loadSettings(self):
        try:
            # load the settings
            apply_over_wifi = self.settings.value("apply_over_wifi", False, type=bool)
            auto_reboot = self.settings.value("auto_reboot", True, type=bool)
            risky_tweaks = self.settings.value("show_risky_tweaks", False, type=bool)
            ignore_frame_limit = self.settings.value("ignore_pb_frame_limit", False, type=bool)
            disable_tendies_limit = self.settings.value("disable_tendies_limit", False, type=bool)
            show_all_spoofable = self.settings.value("show_all_spoofable_models", False, type=bool)
            restore_truststore = self.settings.value("restore_truststore", False, type=bool)
            br_transfer_mode = self.settings.value("bookrestore_transfer_mode", 0, type=int)
            skip_setup = self.settings.value("skip_setup", True, type=bool)
            supervised = self.settings.value("supervised", False, type=bool)
            organization_name = self.settings.value("organization_name", "", type=str)

            self.ui.allowWifiApplyingChk.setChecked(apply_over_wifi)
            self.ui.autoRebootChk.setChecked(auto_reboot)
            self.ui.showRiskyChk.setChecked(risky_tweaks)
            self.ui.ignorePBFrameLimitChk.setChecked(ignore_frame_limit)
            self.ui.disableTendiesLimitChk.setChecked(disable_tendies_limit)
            self.ui.showAllSpoofableChk.setChecked(show_all_spoofable)
            self.ui.trustStoreChk.setChecked(restore_truststore)
            self.ui.brTransferModeDrp.setCurrentIndex(br_transfer_mode)
            self.ui.skipSetupChk.setChecked(skip_setup)
            self.ui.supervisionChk.setChecked(supervised)
            self.ui.supervisionOrganization.setText(organization_name)

            # hide/show the warning label
            if skip_setup:
                self.ui.skipSetupOnLbl.show()
            else:
                self.ui.skipSetupOnLbl.hide()

            # hide/show the frame limit
            if risky_tweaks:
                self.ui.ignorePBFrameLimitChk.show()
                self.ui.disableTendiesLimitChk.show()
            else:
                self.ui.ignorePBFrameLimitChk.hide()
                self.ui.disableTendiesLimitChk.hide()

            self.device_manager.apply_over_wifi = apply_over_wifi
            self.device_manager.auto_reboot = auto_reboot
            self.device_manager.allow_risky_tweaks = risky_tweaks
            video_handler.set_ignore_frame_limit(ignore_frame_limit)
            self.device_manager.show_all_spoofable_models = show_all_spoofable
            self.device_manager.disable_tendies_limit = disable_tendies_limit
            self.device_manager.restore_truststore = restore_truststore
            self.device_manager.bookrestore_transfer_mode = BookRestoreFileTransferMethod(br_transfer_mode)
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
        self.ui.mgaScrollArea.verticalScrollBar().setValue(0) # reset scroll to top
        self.ui.pages.setCurrentIndex(Page.Gestalt.value)

    def on_featureFlagsPageBtn_clicked(self):
        self.pages[Page.FeatureFlags].load()
        self.ui.pages.setCurrentIndex(Page.FeatureFlags.value)
    
    def on_euEnablerPageBtn_clicked(self):
        self.pages[Page.EUEnabler].load()
        self.ui.pages.setCurrentIndex(Page.EUEnabler.value)

    def on_statusBarPageBtn_clicked(self):
        self.pages[Page.StatusBar].load()
        self.ui.sbScrollArea.verticalScrollBar().setValue(0) # reset scroll to top
        self.ui.pages.setCurrentIndex(Page.StatusBar.value)

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

    def on_templatesPageBtn_clicked(self):
        self.pages[Page.Templates].load()
        self.ui.pages.setCurrentIndex(Page.Templates.value)

    def on_advancedPageBtn_clicked(self):
        self.pages[Page.RiskyTweaks].load()
        self.ui.pages.setCurrentIndex(Page.RiskyTweaks.value)

    def on_miscOptionsBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.MiscOptions.value)

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


    ## APPLY PAGE
    def on_chooseGestaltBtn_clicked(self):
        selected_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Mobile Gestalt File", "", "Plist Files (*.plist)", options=QtWidgets.QFileDialog.ReadOnly)
        if selected_file == "" or selected_file == None:
            self.device_manager.data_singleton.gestalt_path = None
            self.ui.gestaltLocationLbl.setText(self.noneText)
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
                not "CacheVersion" in gestalt_plist
                or not "0+nc/Udy4WNG8S+Q7a/s1A" in gestalt_plist["CacheExtra"]
                or gestalt_plist["CacheVersion"] != self.device_manager.data_singleton.current_device.build
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
        dialog = ResetDialog(device_manager=self.device_manager, apply_reset=self.apply_changes)
        dialog.exec()

    @QtCore.Slot()
    def on_applyTweaksBtn_clicked(self):
        self.apply_changes()

    def apply_changes(self, reset_pages: list=None):
        if not self.apply_in_progress:
            self.apply_in_progress = True
            self.toggle_thread_btns(disabled=True)
            self.worker_thread = ApplyThread(manager=self.device_manager, settings=self.settings, reset_pages=reset_pages)
            self.worker_thread.progress.connect(self.ui.statusLbl.setText)
            self.worker_thread.alert.connect(self.alert_message)
            self.worker_thread.finished.connect(self.finish_apply_thread)
            self.worker_thread.finished.connect(self.worker_thread.deleteLater)
            self.worker_thread.start()
    def alert_message(self, alert: ApplyAlertMessage | None, log_to_console: bool = True):
        if alert is None:
            # do sudo dialog input
            get_sudo_pwd() # clear if it is already there
            pwd, ok = QtWidgets.QInputDialog.getText(None, "Enter Password for Sudo", "Sudo Password:", QtWidgets.QLineEdit.Password, "")
            if ok and pwd:
                set_sudo_pwd(pwd)
            set_sudo_complete(True)
            return
        if log_to_console:
            print(alert.txt)
        detailsBox = QtWidgets.QMessageBox()
        detailsBox.setIcon(alert.icon)
        detailsBox.setWindowTitle(alert.title)
        detailsBox.setText(alert.txt)
        if alert.detailed_txt != None:
            detailsBox.setDetailedText(alert.detailed_txt)
        detailsBox.exec()

    def finish_apply_thread(self):
        self.apply_in_progress = False
        self.toggle_thread_btns(disabled=False)
    def toggle_thread_btns(self, disabled: bool):
        if disabled or not self.apply_in_progress:
            self.ui.applyTweaksBtn.setDisabled(disabled)
            self.ui.removeTweaksBtn.setDisabled(disabled)
        if disabled or not self.refresh_in_progress:
            self.ui.refreshBtn.setDisabled(disabled)
