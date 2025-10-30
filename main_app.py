print("Starting Nugget...")

import sys
import os
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import QLocale, QSettings

from controllers.translator import Translator
from gui.main_window import MainWindow
from devicemanagement.device_manager import DeviceManager
from tweaks.tweaks import tweaks, TweakID

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    dm = DeviceManager()

    # Load language settings
    settings = QSettings("Nugget", "settings")
    translator = Translator(app, settings)
    translator.set_default_locale(translator.get_saved_locale_code())
    translator.load_translations()

    # Set icon (works with PyInstaller + from source)
    icon_path = os.path.join(getattr(sys, "_MEIPASS", os.path.dirname(__file__)), "nugget.ico")
    app.setWindowIcon(QtGui.QIcon(icon_path))

    widget = MainWindow(device_manager=dm, translator=translator)
    translator.fix_ui_for_rtl(widget.ui)
    widget.resize(800, 600)
    widget.show()

    # Handle file args (e.g. drag & drop)
    for arg in sys.argv:
        if arg.endswith('.tendies'):
            tweaks[TweakID.PosterBoard].add_tendie(arg)
        elif arg.endswith('.batter'):
            tweaks[TweakID.Templates].add_template(arg)

    print("Nugget launched.")
    sys.exit(app.exec())