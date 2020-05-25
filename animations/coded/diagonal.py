from config import *
from lib import cords, led
from utils.time import *


def diagonal(gen):
    highest = DISPLAY_ROWS + DISPLAY_COLUMNS
    for i in range(highest):
        positions = []
        for j in range(i):
            positions.append(cords.Cords(i - j - 1, j))
        led.singe_pixel(gen.generate(), *positions)
        sleep_ms(100)
