from config import *
from lib import led, cords
from utils.time import *


def snake(color, horizontal=True):
    rows = DISPLAY_ROWS if horizontal else DISPLAY_COLUMNS
    cols = DISPLAY_COLUMNS if horizontal else DISPLAY_ROWS
    for raw_y in range(rows):
        for raw_x in range(cols):
            y = raw_y
            x = raw_x if y % 2 == 0 else cols - raw_x - 1
            if not horizontal:
                (x, y) = (y, x)
            led.singe_pixel(color, cords.Cords(x, y))
            sleep_ms(50)
