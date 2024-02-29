import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Dialog Example")
        self.setGeometry(100, 100, 400, 200)

        self.button = QPushButton("Open File Dialog", self)
        self.button.setGeometry(150, 50, 200, 50)
        self.button.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        fileName, _ = QFileDialog.getOpenFileNames(self, "Open File", "", "All Files (*)")
        if fileName:
            print("Selected file:", fileName)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
