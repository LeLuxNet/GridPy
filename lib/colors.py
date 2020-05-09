import random

import neopixel

from config import *


class Color:

    def __init__(self, red, green, blue, brightness=BRIGHTNESS_NORMAL):
        self.red = red
        self.green = green
        self.blue = blue
        self.brightness = brightness

    def __int__(self):
        return neopixel.Color(int(self.green * self.brightness),
                              int(self.red * self.brightness),
                              int(self.blue * self.brightness))  # Red and green are switched


COLOR_BLACK = Color(0, 0, 0)
COLOR_WHITE = Color(255, 255, 255)

COLOR_WHITE_WARM = Color(255, 255, 100)

COLOR_RED = Color(255, 0, 0)
COLOR_GREEN = Color(0, 255, 0)
COLOR_BLUE = Color(0, 0, 255)

BRIGHTNESS_NONE = 1

BG = None
FG = COLOR_WHITE


def random_color():
    return Color(random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255))


def set_bg(color):
    global BG
    BG = color


def get_bg():
    return BG


def set_fg(color):
    global FG
    FG = color


def get_fg():
    return FG
