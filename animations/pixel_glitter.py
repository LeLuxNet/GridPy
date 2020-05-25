import random

from config import *
from lib import led, colors
from utils.time import *


def pixel_glitter_random():
    free = led.DISPLAY_PIXELS[:]
    for i in range(DISPLAY_COUNT):
        pos = free[random.randint(0, len(free) - 1)]
        led.singe_pixel(colors.random_color(), pos)
        free.remove(pos)
        sleep_ms(50)
    sleep_ms(500)
