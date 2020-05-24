from PIL import Image

from lib import cords
from lib.colors import *

DISPLAY_PIXELS = []
for i in range(LED_COUNT):
    if cords.from_index(i).visible():
        DISPLAY_PIXELS.append(i)


def fill(color):
    for i in DISPLAY_PIXELS:
        draw_pixel(i, color)
    strip.show()


def fill_func(func):
    for i in DISPLAY_PIXELS:
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
    img = img.resize((DISPLAY_COLUMNS, DISPLAY_ROWS), Image.NEAREST)
    background = Image.new("RGB", img.size, (0, 0, 0))
    mask = None
    if img.split() == 4:
        mask = img.split()[3]
    background.paste(img, mask=mask)
    for i, pixel in enumerate(background.getdata()):
        pos = cords.Cords(i % DISPLAY_COLUMNS, i // DISPLAY_COLUMNS)
        draw_pixel(pos, Color(pixel[0], pixel[1], pixel[2]))
    strip.show()


def clear():
    fill(COLOR_BLACK)


strip = neopixel.NeoPixel(LED_PIN, LED_COUNT, auto_write=False, pixel_order=LED_PIXEL_ORDER)
