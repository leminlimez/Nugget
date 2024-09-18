import sys
from PySide6 import QtCore, QtWidgets

from gui.main_window import MainWindow
from devicemanagement.device_manager import DeviceManager

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    dm = DeviceManager()
    dm.get_devices()

    widget = MainWindow(device_manager=dm)
    widget.resize(800, 600)
    widget.show()
    
    sys.exit(app.exec())