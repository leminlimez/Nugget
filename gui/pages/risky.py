from .page import Page
from qt.ui_mainwindow import Ui_Nugget

from tweaks.tweaks import tweaks

class RiskyPage(Page):
    def __init__(self, ui: Ui_Nugget):
        super().__init__()
        self.ui = ui

    def load_page(self):
        self.ui.disableOTAChk.toggled.connect(self.on_disableOTAChk_clicked)
        self.ui.enableResolutionChk.toggled.connect(self.on_enableResolutionChk_clicked)
        self.ui.resHeightTxt.textEdited.connect(self.on_resHeightTxt_textEdited)
        self.ui.resWidthTxt.textEdited.connect(self.on_resWidthTxt_textEdited)
        self.ui.resChangerContent.hide()
        self.ui.resHeightWarningLbl.hide()
        self.ui.resWidthWarningLbl.hide()

    ## ACTIONS
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