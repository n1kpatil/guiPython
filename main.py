import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main_window import Ui_MainWindow  # Generated from your .ui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons to functions
        self.ui.pushButton.clicked.connect(lambda: self.button_clicked("pushButton"))
        self.ui.pushButton_2.clicked.connect(lambda: self.button_clicked("pushButton_2"))
        self.ui.pushButton_3.clicked.connect(lambda: self.button_clicked("pushButton_3"))

   # def button_clicked(self, label):
    #    print(f"{label} was clicked!")
    #   self.setWindowTitle(label)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
