import pygame

from hardware import base
from lib.colors import *

MAX_SIZE = 500

if LED_COLUMNS > LED_ROWS:
    WIDTH = MAX_SIZE
    HEIGHT = int(WIDTH / LED_COLUMNS * LED_ROWS)
else:
    HEIGHT = MAX_SIZE
    WIDTH = int(HEIGHT / LED_ROWS * LED_COLUMNS)

PIXEL_WIDTH = WIDTH / LED_COLUMNS
PIXEL_HEIGHT = HEIGHT / LED_ROWS

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class LedLib(base.LedLib):

    def set_pixel(self, pos, color):
        pygame.event.pump()
        rect = pygame.Rect((PIXEL_WIDTH * pos.x, PIXEL_HEIGHT * pos.y),
                           (PIXEL_HEIGHT + 1, PIXEL_WIDTH + 1))
        pygame.draw.rect(screen, color.get(), rect)

    def show(self):
        pygame.event.pump()
        pygame.display.update()


class ButtonLib(base.ButtonLib):

    def pressed(self, button):
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        return keys[button.id + 97]
