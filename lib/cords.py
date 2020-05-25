import random

from config import *


class Cords:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __int__(self):
        if not self.visible():
            return -1
        if _is_reversed_row(self.y):
            return (self.y + 1) * LED_COLUMNS - self.x - 1
        return self.y * LED_COLUMNS + self.x

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return str(self.x) + "X " + str(self.y) + "Y"

    def visible(self):
        return DISPLAY_ROWS > self.y >= 0 and DISPLAY_COLUMNS > self.x >= 0

    def flip(self):
        (self.x, self.y) = (self.y, self.x)


def _is_reversed_row(row):
    return LED_REVERSED and row % 2 == 1


def _calc_row(i):
    return i // LED_COLUMNS


def _calc_col(i):
    if _is_reversed_row(_calc_row(i)):
        return LED_COLUMNS - i % LED_COLUMNS - 1
    return i % LED_COLUMNS


def from_index(i):
    return Cords(_calc_col(i), _calc_row(i))


def random_cords():
    x = random.randint(0, DISPLAY_COLUMNS)
    y = random.randint(0, DISPLAY_ROWS)
    return Cords(x, y)
