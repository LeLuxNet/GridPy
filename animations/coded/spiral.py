from animations import color
from config import *
from lib import led, cords
from utils.time import sleep, sleep_ms


def _calc_amount():
    return min(DISPLAY_ROWS, DISPLAY_COLUMNS) // 2


def _draw_rect(pos1, pos2, color, time=0):
    for j in range(pos1.x, pos2.x):
        led.singe_pixel(color, cords.Cords(j, pos1.y))
        sleep_ms(time)
    for j in range(pos1.y, pos2.y):
        led.singe_pixel(color, cords.Cords(pos2.x, j))
        sleep_ms(time)
    for j in range(pos2.x, pos1.x, -1):
        led.singe_pixel(color, cords.Cords(j, pos2.y))
        sleep_ms(time)
    for j in range(pos2.y, pos1.y, -1):
        led.singe_pixel(color, cords.Cords(pos1.x, j))
        sleep_ms(time)


def spiral(gen, time=50):
    for i in range(_calc_amount()):
        _draw_rect(cords.Cords(i, i),
                   cords.Cords(DISPLAY_COLUMNS - i - 1, DISPLAY_ROWS - i - 1),
                   gen.generate(), time)


def zoom(gen, steps):
    length = _calc_amount() + steps
    cols = color.ListGenerator(gen.generate_list(length))
    for i in range(length):
        cols.index = i
        spiral(cols, time=0)
        sleep(1)


def spiral_zoom(gen, steps):
    col = gen.generate_list(_calc_amount() + steps)
    spiral(color.ListGenerator(col), 50)
    col.pop()
    zoom(color.ListGenerator(col), steps)
