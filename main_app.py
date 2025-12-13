import sys
import os
import multiprocessing
import runpy
import warnings
import traceback

# 1. SILENCE WARNINGS
warnings.filterwarnings("ignore")

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import QLocale, QSettings

from controllers.translator import Translator
from gui.main_window import MainWindow
from devicemanagement.device_manager import DeviceManager
from tweaks.tweaks import tweaks, TweakID

if __name__ == "__main__":
    multiprocessing.freeze_support()

    # 2. CLI DISPATCHER
    if len(sys.argv) > 1:
        if '-m' in sys.argv:
            try:
                m_index = sys.argv.index('-m')
                # Args: [module_name, arg1, arg2...]
                sys.argv = sys.argv[m_index+1:]
                module_name = sys.argv[0]

                try:
                    # Attempt 1: Run standard module
                    runpy.run_module(module_name, run_name="__main__", alter_sys=True)
                except ImportError as e:
                    # Attempt 2: Handle "is a package" error by targeting __main__ explicitly
                    if "cannot be directly executed" in str(e) or "No module named" in str(e):
                         runpy.run_module(f"{module_name}.__main__", run_name="__main__", alter_sys=True)
                    else:
                        raise

            except Exception as e:
                # Print error to stderr so the main process can read it
                sys.stderr.write(f"Background Process Crash: {e}\n")
                traceback.print_exc()
            sys.exit()

        first_arg = sys.argv[1]
        if first_arg.endswith('.py') and not first_arg.lower().endswith(('.tendies', '.batter')):
            sys.argv = sys.argv[1:]
            try:
                runpy.run_path(sys.argv[0], run_name="__main__")
            except Exception as e:
                sys.stderr.write(f"Script Crash: {e}\n")
                traceback.print_exc()
            sys.exit()

    # 3. GUI STARTUP
    print("Starting Nugget...")
    
    app = QtWidgets.QApplication([])
    dm = DeviceManager()

    settings = QSettings("Nugget", "settings")
    translator = Translator(app, settings)
    translator.set_default_locale(translator.get_saved_locale_code())
    translator.load_translations()

    icon_path = os.path.join(getattr(sys, "_MEIPASS", os.path.dirname(__file__)), "nugget.ico")
    app.setWindowIcon(QtGui.QIcon(icon_path))

    widget = MainWindow(device_manager=dm, translator=translator)
    translator.fix_ui_for_rtl(widget.ui)
    widget.resize(800, 600)
    widget.show()

    for arg in sys.argv:
        if arg.endswith('.tendies'):
            tweaks[TweakID.PosterBoard].add_tendie(arg)
        elif arg.endswith('.batter'):
            tweaks[TweakID.Templates].add_template(arg)

    print("Nugget launched.")
    sys.exit(app.exec())