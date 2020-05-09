import random

import neopixel


class Color:

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __int__(self):
        return neopixel.Color(self.green, self.red, self.blue)  # Red and green are switched


COLOR_BLACK = Color(0, 0, 0)
COLOR_WHITE = Color(255, 255, 255)

COLOR_RED = Color(255, 0, 0)
COLOR_GREEN = Color(0, 255, 0)
COLOR_BLUE = Color(0, 0, 255)

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
