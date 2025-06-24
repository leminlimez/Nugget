print("Starting Nugget...")

import sys
import os
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import QLocale, QSettings

from controllers.translator import Translator
from gui.main_window import MainWindow
from devicemanagement.device_manager import DeviceManager
from tweaks.tweaks import tweaks

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    dm = DeviceManager()

    # load the language settings
    settings = QSettings("Nugget", "settings")
    translator = Translator(app, settings)
    translator.set_default_locale(translator.get_saved_locale_code())
    
    # load translations
    translator.load_translations()

    # set icon
    icon = QtGui.QIcon("nugget.ico")
    app.setWindowIcon(icon)

    widget = MainWindow(device_manager=dm, translator=translator)
    translator.fix_ui_for_rtl(widget.ui)
    widget.resize(800, 600)
    widget.show()

    # import files from args
    for arg in sys.argv:
        if arg.endswith('.tendies'):
            # add tendies file
            tweaks["PosterBoard"].add_tendie(arg)
        elif arg.endswith('.batter'):
            # add batter file
            tweaks["Templates"].add_template(arg)
    
    print("Nugget launched.")
    sys.exit(app.exec())