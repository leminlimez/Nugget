print("Starting Nugget...")

import sys
from PySide6 import QtGui, QtWidgets

from gui.main_window import MainWindow
from devicemanagement.device_manager import DeviceManager
from tweaks.tweaks import tweaks

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    dm = DeviceManager()

    # set icon
    icon = QtGui.QIcon("nugget.ico")
    app.setWindowIcon(icon)

    widget = MainWindow(device_manager=dm)
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