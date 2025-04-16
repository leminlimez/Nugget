from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import Qt


class MultiComboBox(QComboBox):
    def __init__(self, parent=None, updateAction=lambda x: None):
        super().__init__(parent)
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.setModel(QStandardItemModel(self))
        self.updateAction = updateAction

        # Connect to the dataChanged signal to update the text
        self.model().dataChanged.connect(self.updateText)

    def addItem(self, text: str, data=None):
        item = QStandardItem()
        item.setText(text)
        item.setEnabled(True)
        item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable)
        item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
        self.model().appendRow(item)

    def addItems(self, items_list: list):
        for text in items_list:
            self.addItem(text)

    def deselectAll(self):
        for i in range(self.model().rowCount()):
            self.model().item(i).setCheckState(Qt.CheckState.Unchecked)

    def updateText(self):
        selected_items = [self.model().item(i).text() for i in range(self.model().rowCount())
                          if self.model().item(i).checkState() == Qt.CheckState.Checked]
        if len(selected_items) == 0:
            self.lineEdit().setText("  None")
        elif len(selected_items) == 1:
            self.lineEdit().setText(f"  {selected_items[0]}")
        else:
            self.lineEdit().setText(f"  ({len(selected_items)})")
        if self.updateAction != None:
            self.updateAction(selected_items)

    def showPopup(self):
        super().showPopup()
        # Set the state of each item in the dropdown
        for i in range(self.model().rowCount()):
            item = self.model().item(i)
            combo_box_view = self.view()
            combo_box_view.setRowHidden(i, False)
            check_box = combo_box_view.indexWidget(item.index())
            if check_box:
                check_box.setChecked(item.checkState() == Qt.CheckState.Checked)

    def hidePopup(self):
        # Update the check state of each item based on the checkbox state
        for i in range(self.model().rowCount()):
            item = self.model().item(i)
            combo_box_view = self.view()
            check_box = combo_box_view.indexWidget(item.index())
            if check_box:
                item.setCheckState(Qt.CheckState.Checked if check_box.isChecked() else Qt.CheckState.Unchecked)
        super().hidePopup()