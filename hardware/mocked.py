import pygame

from hardware import base
from lib.colors import *

WIDTH = 500
HEIGHT = int(WIDTH / LED_COLUMNS * LED_ROWS)

PIXEL_WIDTH = WIDTH / LED_COLUMNS
PIXEL_HEIGHT = HEIGHT / LED_ROWS

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class LedLib(base.LedLib):

    def set_pixel(self, pos, color):
        rect = pygame.Rect((PIXEL_WIDTH * pos.x, PIXEL_HEIGHT * pos.y), (PIXEL_HEIGHT, PIXEL_WIDTH))
        pygame.draw.rect(screen, color.get(), rect)

    def show(self):
        pygame.display.update()


class ButtonLib(base.ButtonLib):

    def pressed(self, button):
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        return keys[button.id + 97]
