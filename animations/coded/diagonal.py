from config import *
from lib import cords, led
from utils.time import *


def diagonal(gen, source=cords.TOP_LEFT):
    highest = DISPLAY_ROWS + DISPLAY_COLUMNS
    for i in range(highest):
        positions = []
        for j in range(i):
            pos = cords.Cords(i - j - 1, j)
            pos.mirror(source - 4)
            positions.append(pos)
        led.singe_pixel(gen.generate(), *positions)
        sleep_ms(100)
