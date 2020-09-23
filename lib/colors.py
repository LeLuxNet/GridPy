import colorsys
import random
from typing import Tuple

from config import *


class Color:

    def __init__(self, red: int, green: int, blue: int, brightness=BRIGHTNESS_NORMAL, decimal: bool = False):
        self._red = _from_dec(red, decimal)
        self._green = _from_dec(green, decimal)
        self._blue = _from_dec(blue, decimal)
        self.brightness = brightness

    def get(self) -> Tuple[int, int, int]:
        return self.red, self._green, self._blue

    @property
    def red(self):
        return int(self._red * self.brightness)

    @property
    def green(self):
        return int(self._green * self.brightness)

    @property
    def blue(self):
        return int(self._blue * self.brightness)

    def __str__(self):
        return '#%02X%02X%02X' % (self.red, self.green, self.blue)

    def __repr__(self):
        return str(self)


def _from_dec(val, decimal):
    if decimal:
        return int(val * 255)
    return val


def rgb(r, g, b) -> Color:
    return Color(r, g, b)


def hsv(h, s, v) -> Color:
    return Color(*colorsys.hsv_to_rgb(h, s, v), decimal=True)


COLOR_BLACK = Color(0, 0, 0)
COLOR_WHITE = Color(255, 255, 255)

COLOR_WHITE_WARM = Color(255, 255, 100)

COLOR_RED = Color(255, 0, 0)
COLOR_GREEN = Color(0, 255, 0)
COLOR_BLUE = Color(0, 0, 255)

COLOR_YELLOW = Color(255, 255, 0)
COLOR_CYAN = Color(0, 255, 255)
COLOR_MAGENTA = Color(255, 0, 255)

COLOR_ORANGE = Color(255, 165, 0)

BRIGHTNESS_NONE = 1

BG = None
FG = COLOR_WHITE


def random_color() -> Color:
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
