import random

import neopixel
from PIL import Image

from config import *
from lib import cords


class Color:

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __int__(self):
        return neopixel.Color(self.green, self.red, self.blue)  # Red and green are switched


COLOR_BLACK = Color(0, 0, 0)
COLOR_WHITE = Color(255, 255, 255)

COLOR_RED = Color(255, 0, 0)
COLOR_GREEN = Color(0, 255, 0)
COLOR_BLUE = Color(0, 0, 255)


def random_color():
    return Color(random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255))


def fill(color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, int(color))
    strip.show()


def fill_func(func):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, int(func(cords.from_index(i))))
    strip.show()


def draw_screen(screen, move_x=0, move_y=0):
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            cord = cords.Cords(x + move_x, y + move_y)
            if not cord.visible():
                continue
            strip.setPixelColor(int(cord), screen[y][x])
    strip.show()


def show_image(path):
    img = Image.open(path)
    img = img.resize((LED_COLUMNS, LED_ROWS), Image.NEAREST)
    background = Image.new("RGB", img.size, (0, 0, 0))
    background.paste(img, mask=img.split()[3])
    for i, pixel in enumerate(background.getdata()):
        pos = cords.Cords(i % LED_COLUMNS, i / LED_COLUMNS)
        strip.setPixelColor(int(pos), int(Color(pixel[0], pixel[1], pixel[2])))
    strip.show()


def clear():
    fill(COLOR_BLACK)


strip = neopixel.Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()
