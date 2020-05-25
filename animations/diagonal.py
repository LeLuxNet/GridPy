from config import *
from lib import cords, led, colors
from utils.time import *


def diagonal_random():
    highest = DISPLAY_ROWS + DISPLAY_COLUMNS
    for i in range(highest):
        positions = []
        for j in range(i):
            positions.append(cords.Cords(i - j - 1, j))
        led.singe_pixel(colors.random_color(), *positions)
        sleep_ms(100)
