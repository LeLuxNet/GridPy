from config import *
from lib import cords, led
from utils.time import sleep_ms


def _is_row(side):
    return side == cords.TOP or side == cords.BOTTOM


def lines(gen, source=cords.TOP):
    side = DISPLAY_ROWS if _is_row(source) else DISPLAY_COLUMNS
    other_side = DISPLAY_COLUMNS if _is_row(source) else DISPLAY_ROWS
    for i in range(side):
        color = gen.generate()
        for j in range(other_side):
            pos = cords.Cords(j, i)
            if source == cords.RIGHT or source == cords.BOTTOM:
                pos.mirror_x()
            if source == cords.LEFT or source == cords.RIGHT:
                pos.flip()
            led._pixel(color, pos)
        led._show()
        sleep_ms(100)
