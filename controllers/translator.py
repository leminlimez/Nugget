import os
import sys

from PySide6.QtCore import QTranslator, QLibraryInfo, QLocale, QSettings
from PySide6.QtWidgets import QApplication

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