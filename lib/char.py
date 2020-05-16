import time

from lib import led
from lib.colors import *

CHARS = {
    "A": [[0, 1, 0], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]],
    "B": [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 1], [1, 1, 0]],
    "C": [[1, 1, 1], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 1]],
    "D": [[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 0]],
    "E": [[1, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 0], [1, 1, 1]],
    "F": [[1, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 0], [1, 0, 0]],
    "G": [[1, 1, 1], [1, 0, 0], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
    "H": [[1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]],
    "I": [[1], [1], [1], [1], [1]],
    "J": [[0, 0, 1], [0, 0, 1], [0, 0, 1], [1, 0, 1], [0, 1, 0]],
    "K": [[1, 0, 1], [1, 1, 0], [1, 0, 0], [1, 1, 0], [1, 0, 1]],
    "L": [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 1]],
    "M": [[1, 0, 0, 0, 1], [1, 1, 0, 1, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1]],
    "N": [[1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 1]],
    "O": [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
    "P": [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 0], [1, 0, 0]],
    "Q": [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1]],
    "R": [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 1, 0], [1, 0, 1]],
    "S": [[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
    "T": [[1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
    "U": [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
    "V": [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0]],
    "W": [[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 1, 0, 1, 1], [1, 0, 0, 0, 1]],
    "x": [[0, 0, 0], [0, 0, 0], [1, 0, 1], [0, 1, 0], [1, 0, 1]],
    "X": [[1, 0, 1], [1, 0, 1], [0, 1, 0], [1, 0, 1], [1, 0, 1]],
    "Y": [[1, 0, 1], [1, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
    "Z": [[1, 1, 1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]],
    "0": [[0, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0]],
    "1": [[0, 1], [1, 1], [0, 1], [0, 1], [0, 1]],
    " ": [[0], [0], [0], [0], [0]]
}


def _colorize(screen):
    colored = []
    for x in screen:
        layer = []
        for y in x:
            if y == 1:
                layer.append(get_fg())
            else:
                layer.append(get_bg())
        colored.append(layer)
    return colored


def char(c):
    if c in CHARS:
        return _colorize(CHARS[c])
    else:
        return _colorize(CHARS[c.upper()])


def string(string, empty_col=False):
    first = True
    r_word = [[], [], [], [], []]
    for raw_char in string:
        r_char = char(raw_char)
        for i, row in enumerate(r_word):
            if not first:
                row.append(get_bg())
            for val in r_char[i]:
                row.append(val)
        first = False
    if empty_col:
        for row in r_word:
            row.append(get_bg())
    return r_word


def gliding_text(text, y=0, fade_in=False, fade_out=False):
    old_bg = get_bg()
    set_bg(COLOR_BLACK)
    rendered = string(text, empty_col=True)
    shifts = len(rendered[0])
    start = 0
    if not fade_out:
        shifts -= LED_COLUMNS
    if fade_in:
        start = -LED_COLUMNS
    for shift in range(start, shifts):
        led.draw_screen(rendered, -shift, y)
        time.sleep(TEXT_GLIDING_DELAY / 1000.0)
    set_bg(old_bg)
