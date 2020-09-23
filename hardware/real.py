import RPi.GPIO as GPIO
import rpi_ws281x

from config import *
from hardware import base
from lib import cords
from lib.colors import Color

types = {
    "RGB": rpi_ws281x.ws.WS2811_STRIP_RGB,
    "RBG": rpi_ws281x.ws.WS2811_STRIP_RBG,
    "GRB": rpi_ws281x.ws.WS2811_STRIP_GRB,
    "GBR": rpi_ws281x.ws.WS2811_STRIP_GBR,
    "BRG": rpi_ws281x.ws.WS2811_STRIP_BRG,
    "BGR": rpi_ws281x.ws.WS2811_STRIP_BGR
}


class LedLib(base.LedLib):

    def __init__(self):
        self.strip = rpi_ws281x.PixelStrip(LED_COUNT, LED_PIN, strip_type=types[LED_TYPE])
        self.strip.begin()

    def set_pixel(self, pos: cords.Cords, color: Color):
        self.strip.setPixelColor(int(pos), rpi_ws281x.Color(*color.get()))

    def show(self):
        self.strip.show()


class ButtonLib(base.ButtonLib):

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

    def setup(self, pin):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def pressed(self, button):
        return GPIO.input(button.pin) == GPIO.HIGH

    def cleanup(self):
        GPIO.cleanup()
