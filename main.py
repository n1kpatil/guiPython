import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from test import Ui_MainWindow  # Keep using your existing test.py
from yourfile_ui import Ui_MainWindow as Ui_SecondWindow  # Replace with your actual UI file


class SecondWindow(QMainWindow):
    def __init__(self, selections):
        super().__init__()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self)

        # selections is a list of strings (or whatever you passed)
        # e.g. display them in a label or start processing
        self.ui.label.setText(" | ".join(selections[0]))
        # Or if you want them individually:
        # first, second, third = selections
        # self.process_all(first, second, third)

    # def process_all(self, a, b, c):
    #     # your logic here
    #     pass

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # keep a ref so it doesn't get GC'd
        self.second_window = None
        self.ui.pushButton.clicked.connect(self.open_second)

    def open_second(self):
        # gather all combo-box values into a list
        combos = [
            self.ui.comboBox_14.currentText(),
            self.ui.comboBox_13.currentText(),
            self.ui.comboBox_12.currentText(),
            # add more as needed…
        ]

        # or, if you prefer named values, use a dict:
        # combos = {
        #     'mode': self.ui.comboBox1.currentText(),
        #     'speed': self.ui.comboBox2.currentText(),
        #     'color': self.ui.comboBox3.currentText(),
        # }

        # pass that list (or dict) into your second window
        self.second_window = SecondWindow(combos)
        self.second_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())