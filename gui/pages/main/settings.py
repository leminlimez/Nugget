from ..page import Page
from qt.ui_mainwindow import Ui_Nugget

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QCoreApplication, QLocale

from tweaks.tweak_loader import load_rdar_fix
from tweaks.tweaks import tweaks
from controllers.video_handler import set_ignore_frame_limit

available_languages = {
    "English": "en",
    "Español": "es",
    "Español (México)": "es_MX",
    "Português": "pt",
    "Français": "fr",
    "Français (Canada)": "fr_CA",
    "Français (Belgium)": "fr_BE",
    "Deutsch": "de",
    "Deutsch (Australia)": "de_AT",
    "Italiano": "it",
    "Русский язык": "ru",
    "日本語": "ja",
    "普通话": "zh_CN",
    "臺灣話": "zh_TW",
    "Tiếng Việt": "vi",
    "ภาษาไทย": "th",
    "한국어": "ko",
    "Polski": "pl",
    "Türkçe": "tr",
    "Magyar": "hu",
    "Nederlands": "nl",
    "Čeština": "cs",
    "Gaeilge": "ga",
    "Indonesian": "id",
    "Български": "bg",
    "العربية": "ar",
    "العربية (Saudi Arabia)": "ar_SA",
    "مَصرى (Egypt)": "ar_EG",
    "Аҧсуа бызшәа": "ab",
}

class SettingsPage(Page):
    def __init__(self, window, ui: Ui_Nugget):
        super().__init__()
        self.window = window
        self.ui = ui
        self.lang_indexes = []

    def load_page(self):
        self.ui.allowWifiApplyingChk.toggled.connect(self.on_allowWifiApplyingChk_toggled)
        self.ui.autoRebootChk.toggled.connect(self.on_autoRebootChk_toggled)
        self.ui.showRiskyChk.toggled.connect(self.on_showRiskyChk_toggled)
        self.ui.showAllSpoofableChk.toggled.connect(self.on_showAllSpoofableChk_toggled)

        self.ui.ignorePBFrameLimitChk.toggled.connect(self.on_ignorePBFrameLimitChk_toggled)
        self.ui.disableTendiesLimitChk.toggled.connect(self.on_disableTendiesLimitChk_toggled)

        self.ui.revertRdarChk.toggled.connect(self.on_revertRdarChk_toggled)

        self.ui.trustStoreChk.toggled.connect(self.on_trustStoreChk_toggled)
        self.ui.skipSetupChk.toggled.connect(self.on_skipSetupChk_toggled)
        self.ui.supervisionChk.toggled.connect(self.on_supervisionChk_toggled)
        self.ui.supervisionOrganization.textEdited.connect(self.on_supervisionOrgTxt_textEdited)
        self.ui.resetPairBtn.clicked.connect(self.on_resetPairBtn_clicked)
        self.ui.pocketPosterHelperBtn.clicked.connect(self.on_pocketPosterHelperBtn_clicked)

        self.load_available_languages()
        self.ui.langDrp.activated.connect(self.on_langDrp_activated)

    # Load available languages
    def load_available_languages(self):
        for language in available_languages.keys():
            self.lang_indexes.append(available_languages[language])
            self.ui.langDrp.addItem(language)
        # load the saved option
        try:
            idx = self.lang_indexes.index(self.window.translator.get_saved_locale_code())
        except:
            idx = 0
        self.ui.langDrp.setCurrentIndex(idx)

    ## ACTIONS
    def on_langDrp_activated(self, index: int):
        new_lang = self.lang_indexes[index]
        if new_lang != self.window.translator.get_saved_locale_code():
            self.window.translator.set_new_language(new_lang, restart=True)

    def on_allowWifiApplyingChk_toggled(self, checked: bool):
        self.window.device_manager.apply_over_wifi = checked
        # save the setting
        self.window.settings.setValue("apply_over_wifi", checked)
    def on_showRiskyChk_toggled(self, checked: bool):
        self.window.device_manager.allow_risky_tweaks = checked
        # save the setting
        self.window.settings.setValue("show_risky_tweaks", checked)
        # toggle the button visibility
        if checked:
            self.ui.advancedPageBtn.show()
            self.ui.ignorePBFrameLimitChk.show()
            self.ui.disableTendiesLimitChk.show()
            try:
                self.ui.resetPBDrp.removeItem(4)
            except:
                pass
            self.ui.resetPBDrp.addItem("PB Extensions")
        else:
            self.ui.advancedPageBtn.hide()
            self.ui.ignorePBFrameLimitChk.hide()
            self.ui.disableTendiesLimitChk.hide()
            try:
                self.ui.resetPBDrp.removeItem(4)
            except:
                pass
    def on_ignorePBFrameLimitChk_toggled(self, checked: bool):
        set_ignore_frame_limit(checked)
        # save the setting
        self.window.settings.setValue("ignore_pb_frame_limit", checked)
    def on_disableTendiesLimitChk_toggled(self, checked: bool):
        self.window.device_manager.disable_tendies_limit = checked
        # save the setting
        self.window.settings.setValue("disable_tendies_limit", checked)
    def on_showAllSpoofableChk_toggled(self, checked: bool):
        self.window.device_manager.show_all_spoofable_models = checked
        # save the setting
        self.window.settings.setValue("show_all_spoofable_models", checked)
        # refresh the list of spoofable models
        self.window.setup_spoofedModelDrp_models()
    def on_autoRebootChk_toggled(self, checked: bool):
        self.window.device_manager.auto_reboot = checked
        # save the setting
        self.window.settings.setValue("auto_reboot", checked)

    def on_revertRdarChk_toggled(self, checked: bool):
        if not 'RdarFix' in tweaks:
            load_rdar_fix(self.window.device_manager.data_singleton.current_device)
        tweaks["RdarFix"].set_enabled(checked)

    def on_trustStoreChk_toggled(self, checked: bool):
        self.window.device_manager.restore_truststore = checked
        # save the setting
        self.window.settings.setValue("restore_truststore", checked)

    def on_skipSetupChk_toggled(self, checked: bool):
        self.window.device_manager.skip_setup = checked
        # save the setting
        self.window.settings.setValue("skip_setup", checked)
        # hide/show the warning label
        if checked:
            self.ui.skipSetupOnLbl.show()
        else:
            self.ui.skipSetupOnLbl.hide()
    def on_supervisionOrgTxt_textEdited(self, text: str):
        self.window.device_manager.organization_name = text
        self.window.settings.setValue("organization_name", text)
    def on_supervisionChk_toggled(self, checked: bool):
        self.window.device_manager.supervised = checked
        # save the setting
        self.window.settings.setValue("supervised", checked)

    # Device Options
    def on_resetPairBtn_clicked(self):
        self.window.device_manager.reset_device_pairing()
    def on_pocketPosterHelperBtn_clicked(self):
        # get app hash for posterboard
        bundle_ids = ["com.apple.PosterBoard"]
        if self.window.device_manager.get_current_device_model().startswith("iPhone"):
            bundle_ids.append("com.apple.CarPlayWallpaper")
        hashes = self.window.device_manager.get_app_hashes(bundle_ids)
        print(hashes)
        try:
            self.window.device_manager.send_app_hashes_afc(hashes)
            QMessageBox.information(None, QCoreApplication.tr("PosterBoard App Hash"), QCoreApplication.tr("Your hash has been transferred to the Pocket Poster app.\n\nOpen up its settings and tap \"Detect\"."))
        except:
            # fall back to copy and paste
            copytxt = QCoreApplication.tr("Copy it and paste it")
            try:
                import pyperclip
                pyperclip.copy(hashes["com.apple.PosterBoard"])
                copytxt = QCoreApplication.tr("It has been copied. Paste it")
            except:
                print("pyperclip not found, not copying to clipboard")
            QMessageBox.information(None, QCoreApplication.tr("PosterBoard App Hash"), QCoreApplication.tr("Your hash is:\n{0}\n\n{1} into the Nugget app where it says \"App Hash\".").format(hashes["com.apple.PosterBoard"], copytxt))