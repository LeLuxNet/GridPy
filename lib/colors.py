import colorsys
import random

from config import *


class Color:

    def __init__(self, red, green, blue, brightness=BRIGHTNESS_NORMAL, decimal=False):
        self.red = _from_dec(red, decimal)
        self.green = _from_dec(green, decimal)
        self.blue = _from_dec(blue, decimal)
        self.brightness = brightness

    def get(self):
        return (int(self.red * self.brightness),
                int(self.green * self.brightness),
                int(self.blue * self.brightness))


def _from_dec(val, decimal):
    if decimal:
        return int(val * 255)
    return val


def rgb(r, g, b):
    return Color(r, g, b)


def hsv(h, s, v):
    return Color(*colorsys.hsv_to_rgb(h, s, v), decimal=True)


COLOR_BLACK = Color(0, 0, 0)
COLOR_WHITE = Color(255, 255, 255)

COLOR_WHITE_WARM = Color(255, 255, 100)

COLOR_RED = Color(255, 0, 0)
COLOR_GREEN = Color(0, 255, 0)
COLOR_BLUE = Color(0, 0, 255)

COLOR_YELLOW = Color(255, 255, 0)

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
