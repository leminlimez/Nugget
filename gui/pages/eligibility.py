from .page import Page
from qt.ui_mainwindow import Ui_Nugget

from tweaks.tweaks import tweaks

class EligibilityPage(Page):
    def __init__(self, window, ui: Ui_Nugget):
        super().__init__()
        self.window = window
        self.ui = ui

    def load_page(self):
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
        
        self.ui.aiEnablerContent.hide()

    ## ACTIONS
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
        if not self.window.device_manager.show_all_spoofable_models and not self.window.device_manager.get_current_device_model().startswith("iPhone"):
            # offset the index for ipads
            idx_to_apply += 6
        tweaks["SpoofModel"].set_selected_option(idx_to_apply, is_enabled=(index != 0))
        tweaks["SpoofHardware"].set_selected_option(idx_to_apply, is_enabled=(index != 0 and self.ui.spoofHardwareChk.isChecked()))
        tweaks["SpoofCPU"].set_selected_option(idx_to_apply, is_enabled=(index != 0 and self.ui.spoofCPUChk.isChecked()))
    def on_spoofHardwareChk_toggled(self, checked: bool):
        tweaks["SpoofHardware"].set_enabled(checked and tweaks["SpoofHardware"].selected_option != 0)
    def on_spoofCPUChk_toggled(self, checked: bool):
        tweaks["SpoofCPU"].set_enabled(checked and tweaks["SpoofCPU"].selected_option != 0)