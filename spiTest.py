#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import spidev, time

spi = spidev.SpiDev()
spi.open(0, 0)               # /dev/spidev0.0
spi.max_speed_hz = 500_000
spi.mode = 0b00
spi.bits_per_word = 8

def send_char(c: str) -> int:
    cmd = ord(c)
    # full-duplex 2-byte transfer:
    resp = spi.xfer2([cmd, 0x00])
    reply = resp[1]
    print(f"Sent '{c}' (0x{cmd:02X}) ? Reply 0x{reply:02X}")
    return reply

try:
    for _ in range(10):
        for ch in "HELLO\n":
            send_char(ch)
            time.sleep(0.01)
finally:
    spi.close()
