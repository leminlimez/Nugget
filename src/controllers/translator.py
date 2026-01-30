import os
import sys

from PySide6.QtCore import QTranslator, QLibraryInfo, QLocale, QSettings
from PySide6.QtWidgets import QApplication

from src.qt.mainwindow_ui import Ui_Nugget

class Translator:
    def __init__(self, app: QApplication, settings: QSettings):
        self.app = app
        self.settings = settings

    def get_saved_locale_code(self) -> str:
        return self.settings.value("locale_code", QLocale.system().languageToCode(QLocale.system().language()), type=str)
    def set_default_locale(self, code: str):
        QLocale.setDefault(QLocale(code))
    def set_new_language(self, code: str, restart: bool = False):
        self.settings.setValue("locale_code", code)
        self.set_default_locale(code)
        self.load_translations()
        if restart:
            os.execl(sys.executable, *sys.orig_argv)
    
    def load_translations(self):
        path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
        translator = QTranslator(self.app)
        if translator.load(QLocale(), 'qtbase', '_', path):
            self.app.installTranslator(translator)
        translator = QTranslator(self.app)
        path = ':/translations'
        if translator.load(QLocale(), 'translations/Nugget', '_', path):
            self.app.installTranslator(translator)

    def fix_ui_for_rtl(self, ui: Ui_Nugget):
        curr_locale = self.get_saved_locale_code()
        if curr_locale == "ar" or curr_locale == "ar_SA" or curr_locale == "ar_EG":
            # need to correct for stuff
            # TOP BAR
            ui.phoneIconBtn.setStyleSheet("QToolButton {\n	border-top-left-radius: 0px;\n	border-bottom-left-radius: 0px;\n}")
            ui.titleBar.setStyleSheet("QToolButton {\n	border-top-right-radius: 0px;\n	border-bottom-right-radius: 0px;\n}")
            # HOME PAGE
            ui.leminTwitterBtn.setStyleSheet("QToolButton {\n	border-top-left-radius: 0px;\n	border-bottom-left-radius: 0px;\n	background: none;\n	border: 1px solid #3b3b3b;\n	border-left: none;\n}\n\nQToolButton:pressed {\n    background-color: #535353;\n    color: #FFFFFF;\n}")
            ui.leminKoFiBtn.setStyleSheet("QToolButton {\n	border-top-right-radius: 0px;\n	border-bottom-right-radius: 0px;\n	background: none;\n	border: 1px solid #3b3b3b;\n}\n\nQToolButton:pressed {\n    background-color: #535353;\n    color: #FFFFFF;\n}")
            ui.posterRestoreBtn.setStyleSheet("QToolButton {\n	border-top-left-radius: 0px;\n	border-bottom-left-radius: 0px;\n	background: none;\n	border: 1px solid #3b3b3b;\n	border-left: none;\n}\n\nQToolButton:pressed {\n    background-color: #535353;\n    color: #FFFFFF;\n}")
            ui.translatorsBtn.setStyleSheet("QToolButton {\n	border-top-left-radius: 0px;\n	border-bottom-left-radius: 0px;\n	background: none;\n	border: 1px solid #3b3b3b;\n	border-left: none;\n}\n\nQToolButton:pressed {\n    background-color: #535353;\n    color: #FFFFFF;\n}")
            ui.mikasaBtn.setStyleSheet("QToolButton {\n	border-top-right-radius: 0px;\n	border-bottom-right-radius: 0px;\n	background: none;\n	border: 1px solid #3b3b3b;\n}\n\nQToolButton:pressed {\n    background-color: #535353;\n    color: #FFFFFF;\n}")
            ui.qtBtn.setStyleSheet("QToolButton {\n	border-top-right-radius: 0px;\n	border-bottom-right-radius: 0px;\n	background: none;\n	border: 1px solid #3b3b3b;\n}\n\nQToolButton:pressed {\n    background-color: #535353;\n    color: #FFFFFF;\n}")