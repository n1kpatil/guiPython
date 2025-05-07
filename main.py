import sys
import numpy as np


# from PyQt5.QtWidgets    import QApplication, QMainWindow

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,      # ← add this
)
from test               import Ui_MainWindow  # Keep using your existing test.py
from plot               import Ui_MainWindow as Ui_SecondWindow  # Replace with your actual UI file
from spi_backend        import SPIBus
from PyQt5.QtCore       import QTimer
import pyqtgraph as pg

# class SecondWindow(QMainWindow):
#     def __init__(self, selections):
#         super().__init__()
#         self.ui = Ui_SecondWindow()
#         self.ui.setupUi(self)
#         self.logicinputLabeling(selections)
#         # set up the plot
#         self.plot = pg.PlotWidget()
#         self.ui.plotContainer.layout().addWidget(self.plot)
#         self.curve = self.plot.plot(self.readSpiData)

#         self.ui.pushButton_13.clicked.connect
#           # initialize SPI (real on Linux, simulated on other OS)
#         self.spi = SPIBus(bus=0, device=0)

#         # rolling buffer for 100 samples
#         self.data = np.zeros(100)

#         # timer to drive live updates
#         self.timer = QTimer(self, interval=50)   # 50 ms → 20 Hz
#         self.timer.timeout.connect(self.update)
#         self.timer.start()

#     def logicinputLabeling(self, selections):   
#         self.ui.pushButton.setText(selections[0])
#         self.ui.pushButton_2.setText(selections[1])
#         self.ui.pushButton_3.setText(selections[2])
#         self.ui.pushButton_4.setText(selections[3])
#         self.ui.pushButton_5.setText(selections[4])
#         self.ui.pushButton_6.setText(selections[5])
#         self.ui.pushButton_7.setText(selections[6])
#         self.ui.pushButton_8.setText(selections[7])

#     def readSpiData(self):
#         self.data 
        
#     # set up the plot
#     def update(self):
#         # shift old samples left
#         self.data[:-1] = self.data[1:]
#         # read a new sample from SPIBus
#         raw = self.spi.read16()
#         # normalize a 12-bit value to 0.0–1.0
#         self.data[-1] = raw / 4095.0
#         # refresh the curve
#         self.curve.setData(self.data)

class SecondWindow(QMainWindow):
    def __init__(self, selections):
        super().__init__()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self)

        # set up plot
        self.plot  = pg.PlotWidget()
        self.ui.plotContainer.layout().addWidget(self.plot)
        self.curve = self.plot.plot()

        # SPI & data buffer
        self.spi  = SPIBus(bus=0, device=0)
        self.data = np.zeros(100)

        # timer but don’t start yet
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)

        # hook up start/stop buttons
        self.ui.pushButton_13.clicked.connect(self.start_updates)

        # any other button click stops the updates
        for btn in self.findChildren(QPushButton):
            if btn is not self.ui.pushButton_13:
                btn.clicked.connect(self.stop_updates)

    def start_updates(self):
        if not self.timer.isActive():
            # match your desired rate; e.g. 100ms
            self.timer.start(100)

    def stop_updates(self):
        if self.timer.isActive():
            self.timer.stop()

    def update(self):
        # fetch the full rolling buffer
        raw = self.spi.request_buffer()              # returns 100 bytes
        arr = np.frombuffer(raw, dtype=np.uint8)     # 0–255
        self.curve.setData(arr)


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
            self.ui.comboBox_7.currentText(),
            self.ui.comboBox_22.currentText(),
            self.ui.comboBox_23.currentText(),
            self.ui.comboBox_24.currentText(),
            self.ui.comboBox_25.currentText(),
            self.ui.comboBox_20.currentText(),
            self.ui.comboBox_21.currentText(),
            self.ui.comboBox_26.currentText(),
            self.ui.comboBox_27.currentText(),
            self.ui.comboBox_30.currentText(),            
            self.ui.comboBox_31.currentText(),            
            self.ui.comboBox_28.currentText(),            
            self.ui.comboBox_29.currentText(),
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