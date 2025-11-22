import sys
if len(sys.argv) < 2 or sys.argv[1] != '--tunnel':
    print("Starting Nugget...")

import os
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import QSettings

from controllers.translator import Translator
from gui.main_window import MainWindow
from devicemanagement.device_manager import DeviceManager
from tweaks.tweaks import tweaks, TweakID
from restore.bookrestore import set_script_path

if __name__ == "__main__":
    # set the path of the script
    set_script_path(os.path.abspath(__file__))
    should_run_app = True
    # bookrestore creating tunnel
    # formats:
    # python main_app.py --tunnel [udid]
    # python main_app.py --tunnel [udid] [stdout file] [stderr file]
    if len(sys.argv) > 2 and sys.argv[1] == '--tunnel':
        # run as admin on windows (for bookrestore)
        relaunched=False
        if os.name == 'nt':
            try:
                import pyuac
                if not pyuac.isUserAdmin():
                    print("Relaunching as Admin")
                    relaunched = True
                    should_run_app = False
                    pyuac.runAsAdmin()
            except:
                pass
        if not relaunched:
            udid = sys.argv[2]
            fout = None
            ferr = None
            if len(sys.argv) > 4:
                fout = sys.argv[3]
                ferr = sys.argv[4]
            from restore.tunneling import create_tunnel
            should_run_app = False
            create_tunnel(udid, fout, ferr)

    # main app launch
    if should_run_app:
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