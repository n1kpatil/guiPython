import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from test import Ui_MainWindow  # Keep using your existing test.py

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.pushButton.clicked.connect(lambda: self.button_clicked("pushButton"))
        # Uncomment if you have these in UI
        # self.ui.pushButton_2.clicked.connect(lambda: self.button_clicked("pushButton_2"))
        # self.ui.pushButton_3.clicked.connect(lambda: self.button_clicked("pushButton_3"))

    def button_clicked(self, label):
        print(f"{label} clicked")
        self.setWindowTitle(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
