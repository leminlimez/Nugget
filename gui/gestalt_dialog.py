from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout

class GestaltDialog(QDialog):
    def __init__(self, device_manager, gestalt_label, selected_file, parent=None):
        super().__init__(parent)
        self.device_manager = device_manager
        self.gestalt_label = gestalt_label
        self.selected_file = selected_file

        QBtn = (
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("The gestalt file looks like it was made for a different device.\nAre you sure you want to use this one?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

    def accept(self):
        self.device_manager.data_singleton.gestalt_path = self.selected_file
        self.gestalt_label.setText(self.selected_file)
        super().accept()