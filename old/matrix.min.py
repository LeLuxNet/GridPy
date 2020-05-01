import time

import neopixel

LED_COUNT = 100
LED_PIN = 18
LED_FREQ = 800000  # 800kHz
LED_DMA = 10
LED_INVERT = False
LED_BRIGHTNESS = 20
LED_CHANNEL = 0


def sleepMs(ms):
    time.sleep(ms / 1000.0)


def run(name):
    file = open("matrix/" + name + ".txt", "r")
    lines = file.readlines()
    for l in lines:
        line = l[1:]
        if l[0] == "d":
            sleepMs(int(line))
        elif l[0] == "c":
            parts = line.split(" ")
            strip.setPixelColor(int(parts[0]), int(parts[1]))
        elif l[0] == "s":
            strip.show()


def init():
    global strip
    strip = neopixel.Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()


if __name__ == "__main__":
    init()
    run(raw_input("Matrix: "))
