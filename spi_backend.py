import sys

if sys.platform.startswith('linux'):
    import spidev

    class SPIBus:
        def __init__(self, bus=0, device=0, max_hz=500_000):
            self.dev = spidev.SpiDev()
            self.dev.open(bus, device)
            self.dev.max_speed_hz = max_hz

        def read16(self):
            raw = self.dev.xfer2([0x00, 0x00])
            return (raw[0] << 8) | raw[1]

else:
    import random

    class SPIBus:
        def __init__(self, *args, **kwargs):
            print("SPIBus: running in simulation mode (no real SPI)")

        def read16(self):
            # simulate a 12-bit reading
            return random.randint(0, 4095)
