import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit


class SettingsWindow(QWidget):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.setWindowTitle('Settings')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.setting_input = QLineEdit(self)
        layout.addWidget(self.setting_input)

        save_button = QPushButton('Save', self)
        save_button.clicked.connect(self.save_settings)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_settings(self):
        # Save settings to file or database
        settings_value = self.setting_input.text()
        # Here, you should save the settings to a file or database
        # For simplicity, I'll just print the setting for demonstration
        print("Settings saved:", settings_value)
        self.close()


class MainWindow(QWidget):
    def __init__(self, settings, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Display the settings in the main window
        self.settings_label = QLineEdit(settings, self)
        self.settings_label.setReadOnly(True)
        layout.addWidget(self.settings_label)

        self.setLayout(layout)


class OpeningWindow(QWidget):
    def __init__(self, parent=None):
        super(OpeningWindow, self).__init__(parent)
        self.setWindowTitle('Opening Window')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        open_main_button = QPushButton('Open Main', self)
        open_main_button.clicked.connect(self.open_main_window)
        layout.addWidget(open_main_button)

        self.setLayout(layout)

    def open_main_window(self):
        # Retrieve settings
        settings_window = SettingsWindow()
        settings_value = settings_window.setting_input.text()
        settings_window.show()
        # Open main window with the retrieved settings
        self.main_window = MainWindow(settings_value)
        self.main_window.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OpeningWindow()
    window.show()
    sys.exit(app.exec())