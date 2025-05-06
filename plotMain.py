import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore    import QTimer
import pyqtgraph as pg

from plot import Ui_MainWindow    # generated via: `pyside6-uic your.ui -o test.py`
from spi_backend import SPIBus

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # embed the plot widget into the 'plotContainer' placeholder
        self.plot = pg.PlotWidget()
        self.ui.plotContainer.layout().addWidget(self.plot)
        self.curve = self.plot.plot()

        # initialize SPI (real on Linux, simulated on other OS)
        self.spi = SPIBus(bus=0, device=0)

        # rolling buffer for 100 samples
        self.data = np.zeros(100)

        # timer to drive live updates
        self.timer = QTimer(self, interval=50)   # 50 ms → 20 Hz
        self.timer.timeout.connect(self.update)
        self.timer.start()

    def update(self):
        # shift old samples left
        self.data[:-1] = self.data[1:]
        # read a new sample from SPIBus
        raw = self.spi.read16()
        # normalize a 12-bit value to 0.0–1.0
        self.data[-1] = raw / 4095.0
        # refresh the curve
        self.curve.setData(self.data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
