from ..page import Page
from qt.mainwindow_ui import Ui_Nugget

from tweaks.tweak_loader import load_eligibility
from tweaks.tweaks import tweaks, TweakID

class EligibilityPage(Page):
    def __init__(self, window, ui: Ui_Nugget):
        super().__init__()
        self.window = window
        self.ui = ui

    def load_page(self):
        self.ui.euEnablerEnabledChk.toggled.connect(self.on_euEnablerEnabledChk_toggled)
        self.ui.methodChoiceDrp.activated.connect(self.on_methodChoiceDrp_activated)
        self.ui.regionCodeTxt.textEdited.connect(self.on_regionCodeTxt_textEdited)

        self.ui.createEligFolderChk.toggled.connect(self.on_createEligFolderChk_toggled)
        self.ui.enableAIChk.toggled.connect(self.on_enableAIChk_toggled)
        self.ui.eligFileChk.toggled.connect(self.on_eligFileChk_toggled)
        self.ui.languageTxt.hide() # to be removed later
        self.ui.languageLbl.hide() # to be removed later
        self.ui.languageTxt.textEdited.connect(self.on_languageTxt_textEdited)
        self.ui.spoofedModelDrp.activated.connect(self.on_spoofedModelDrp_activated)
        self.ui.spoofHardwareChk.toggled.connect(self.on_spoofHardwareChk_toggled)
        self.ui.spoofCPUChk.toggled.connect(self.on_spoofCPUChk_toggled)
        
        self.ui.aiEnablerContent.hide()

        load_eligibility(self.window.device_manager.data_singleton.current_device)

    ## ACTIONS
    def on_euEnablerEnabledChk_toggled(self, checked: bool):
        tweaks[TweakID.EUEnabler].set_enabled(checked)
    def on_methodChoiceDrp_activated(self, index: int):
        tweaks[TweakID.EUEnabler].set_selected_option(index)
    def on_regionCodeTxt_textEdited(self, text: str):
        tweaks[TweakID.EUEnabler].set_region_code(text)

    def on_enableAIChk_toggled(self, checked: bool):
        # tweaks[TweakID.AIEligibility].set_enabled(checked)
        tweaks[TweakID.AIGestalt].set_enabled(checked)
        # change the visibility of stuff
        if checked:
            self.ui.aiEnablerContent.show()
        else:
            self.ui.aiEnablerContent.hide()

    def on_createEligFolderChk_toggled(self, checked: bool):
        tweaks[TweakID.CreateBRFolders].set_enabled(checked)
        self.ui.createFFFolderChk.setChecked(checked)
    def on_eligFileChk_toggled(self, checked: bool):
        tweaks[TweakID.AIEligibility].set_enabled(checked)
        tweaks[TweakID.AIFeatureFlags].set_enabled(checked)
        tweaks[TweakID.AIFeatureFlagsUI].set_enabled(checked)
        if checked:
            self.ui.languageTxt.show()
            self.ui.languageLbl.show()
        else:
            self.ui.languageTxt.hide()
            self.ui.languageLbl.hide()

    def on_languageTxt_textEdited(self, text: str):
        tweaks[TweakID.AIEligibility].set_language_code(text)
    
    def on_spoofedModelDrp_activated(self, index: int):
        idx_to_apply = index
        if not self.window.device_manager.pref_manager.show_all_spoofable_models and not self.window.device_manager.get_current_device_model().startswith("iPhone"):
            # offset the index for ipads
            idx_to_apply += 6
        tweaks[TweakID.SpoofModel].set_selected_option(idx_to_apply, is_enabled=(index != 0))
        tweaks[TweakID.SpoofHardware].set_selected_option(idx_to_apply, is_enabled=(index != 0 and self.ui.spoofHardwareChk.isChecked()))
        tweaks[TweakID.SpoofCPU].set_selected_option(idx_to_apply, is_enabled=(index != 0 and self.ui.spoofCPUChk.isChecked()))
    def on_spoofHardwareChk_toggled(self, checked: bool):
        tweaks[TweakID.SpoofHardware].set_enabled(checked and tweaks[TweakID.SpoofHardware].selected_option != 0)
    def on_spoofCPUChk_toggled(self, checked: bool):
        tweaks[TweakID.SpoofCPU].set_enabled(checked and tweaks[TweakID.SpoofCPU].selected_option != 0)