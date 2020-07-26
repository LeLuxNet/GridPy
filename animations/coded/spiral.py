from animations import color
from config import *
from lib import cords, led
from utils.time import sleep, sleep_ms


def __calc_amount():
    return min(DISPLAY_ROWS, DISPLAY_COLUMNS) // 2


def __draw_rect(pos1, pos2, color, time):
    positions = __get_rect(pos1, pos2)
    if time == 0:
        for pos in positions:
            led._pixel(color, pos)
    else:
        for pos in positions:
            led.pixel(color, pos)
            sleep_ms(time)


def __get_rect(pos1, pos2):
    positions = []
    for j in range(pos1.x, pos2.x):
        positions.append(cords.Cords(j, pos1.y))
    for j in range(pos1.y, pos2.y):
        positions.append(cords.Cords(pos2.x, j))
    for j in range(pos2.x, pos1.x, -1):
        positions.append(cords.Cords(j, pos2.y))
    for j in range(pos2.y, pos1.y, -1):
        positions.append(cords.Cords(pos1.x, j))
    return positions


def spiral(gen, time=50):
    for i in range(__calc_amount()):
        __draw_rect(cords.Cords(i, i),
                    cords.Cords(DISPLAY_COLUMNS - i - 1, DISPLAY_ROWS - i - 1),
                    gen.generate(), time)
    if time == 0:
        led._show()


def zoom(gen, steps):
    length = __calc_amount() + steps
    cols = color.ListGenerator(gen.generate_list(length))
    for i in range(steps):
        cols.index = i
        spiral(cols, 0)
        sleep_ms(500)


def spiral_zoom(gen, steps, replay_first=False):
    if replay_first:
        steps += 1
    col = gen.generate_list(__calc_amount() + steps)
    spiral(color.ListGenerator(col), 50)
    if not replay_first:
        col.pop(1)
    zoom(color.ListGenerator(col), steps)
