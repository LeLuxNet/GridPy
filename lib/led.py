from PIL import Image

from lib import cords
from lib.colors import *


def fill(color):
    strip.fill(color.get())


def fill_func(func):
    for i in range(len(strip)):
        draw_pixel(i, func(cords.from_index(i)))
    strip.show()


def draw_pixel(pos, color):
    if color is not None:
        strip[int(pos)] = color.get()


def draw_screen(screen, move_x=0, move_y=0):
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            cord = cords.Cords(x + move_x, y + move_y)
            if not cord.visible():
                continue
            draw_pixel(cord, screen[y][x])
    strip.show()


def show_image(path):
    img = Image.open(path)
    img = img.resize((LED_COLUMNS, LED_ROWS), Image.NEAREST)
    background = Image.new("RGB", img.size, (0, 0, 0))
    background.paste(img, mask=img.split()[3])
    for i, pixel in enumerate(background.getdata()):
        pos = cords.Cords(i % LED_COLUMNS, i // LED_COLUMNS)
        draw_pixel(pos, Color(pixel[0], pixel[1], pixel[2]))
    strip.show()


def clear():
    fill(COLOR_BLACK)


strip = neopixel.NeoPixel(LED_PIN, LED_COUNT, auto_write=False, pixel_order=LED_PIXEL_ORDER)
