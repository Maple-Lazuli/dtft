import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog


class OpeningWindow(QWidget):
    def __init__(self, parent=None):
        super(OpeningWindow, self).__init__(parent)
        self.setWindowTitle('File Select')
        self.setGeometry(100, 100, 300, 200)
        self.settings_dict = dict()
        layout = QVBoxLayout()

        self.file_select = QPushButton("Open File Dialog", self)
        layout.addWidget(self.file_select)

        self.setLayout(layout)

    def open_file_dialog(self):
        fileNames, _ = QFileDialog.getOpenFileNames(self, "Open File", "", "All Files (*)")
        if fileNames:
            print("Selected file:", fileNames)
            self.settings_dict['files'] = fileNames

    def