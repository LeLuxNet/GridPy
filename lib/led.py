from PIL import Image

from hardware import led_lib
from lib import cords
from lib.colors import *

DISPLAY_PIXELS = []
for i in range(LED_COUNT):
    cord = cords.from_index(i)
    if cord.visible():
        DISPLAY_PIXELS.append(cord)


def fill(color):
    for i in DISPLAY_PIXELS:
        led_lib.set_pixel(i, color)
    led_lib.show()


def fill_func(func):
    for i in DISPLAY_PIXELS:
        led_lib.set_pixel(i, func(i))
    led_lib.show()


def _pixel(color, pos):
    led_lib.set_pixel(pos, color)


def pixel(color, pos):
    led_lib.set_pixel(pos, color)
    led_lib.show()


def _show():
    led_lib.show()


def draw_screen(screen, move_x=0, move_y=0):
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            cord = cords.Cords(x + move_x, y + move_y)
            if not cord.visible():
                continue
            led_lib.set_pixel(cord, screen[y][x])
    led_lib.show()


def show_image(path):
    img = Image.open(path)
    img = img.resize((DISPLAY_COLUMNS, DISPLAY_ROWS), Image.NEAREST)
    background = Image.new("RGB", img.size, (0, 0, 0))
    mask = None
    if img.split() == 4:
        mask = img.split()[3]
    background.paste(img, mask=mask)
    for i, pixel in enumerate(background.getdata()):
        pos = cords.Cords(i % DISPLAY_COLUMNS, i // DISPLAY_COLUMNS)
        led_lib.set_pixel(pos, Color(pixel[0], pixel[1], pixel[2]))
    led_lib.show()


def clear():
    fill(COLOR_BLACK)
