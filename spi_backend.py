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
        
        def request_buffer(self) -> bytes:
            """
            Tell the Arduino to dump its 100‐byte rolling buffer, then clock out
            100 bytes by sending zeros. Returns what came back on MISO.
            """
            # Step 1: trigger the Arduino by sending 'p'
            self.dev.xfer2([ord('p')])
            # Step 2: clock out 100 bytes; master must send something each byte,
            # so we send 0x00 100 times and capture whatever the slave returns.
            resp = self.dev.xfer2([0x00] * 100)
            # resp is now a list of 100 ints in [0..255]
            return bytes(resp)  # or just return resp if you prefer a list of ints

else:
    import random

    class SPIBus:
        def __init__(self, *args, **kwargs):
            print("SPIBus: running in simulation mode (no real SPI)")

        def read16(self):
            # simulate a 12-bit reading
            return random.randint(0, 4095)
