import datetime
import math
import random

from config import *
from lib import app, cords, button, led
from utils import time


class Direction:

    def __init__(self, x, y, left=None, right=None):
        self.x = x
        self.y = y
        self.left = left
        self.right = right


SPEED = 1000

DIR_UP = Direction(0, -1)
DIR_DOWN = Direction(0, 1)
DIR_LEFT = Direction(-1, 0, DIR_DOWN, DIR_UP)
DIR_RIGHT = Direction(1, 0, DIR_UP, DIR_DOWN)

DIR_UP.left = DIR_LEFT
DIR_UP.right = DIR_RIGHT
DIR_DOWN.left = DIR_LEFT
DIR_DOWN.right = DIR_RIGHT


class App(app.BaseApp):

    def __init__(self):
        super().__init__("Snake")
        middle = DISPLAY_ROWS // 2
        self.snake = [
            cords.Cords(3, middle),
            cords.Cords(2, middle),
            cords.Cords(1, middle)
        ]
        self.food = None
        self.gen_food()
        self.direction = DIR_RIGHT

    def run(self):
        self.render()
        while True:
            begin = datetime.datetime.now()
            final_press = None
            try:
                while time.to_ms(datetime.datetime.now() - begin) < SPEED:
                    press = button.any_button_once()
                    if press:
                        final_press = press
            except KeyboardInterrupt:
                break
            if final_press is not None:
                if final_press[0] == 0:
                    self.direction = self.direction.left
                elif final_press[0] == 1:
                    self.direction = self.direction.right
            old_head = self.snake[0]
            head = cords.Cords(old_head.x + self.direction.x, old_head.y + self.direction.y)
            if 0 > head.x or DISPLAY_COLUMNS <= head.x or 0 > head.y or DISPLAY_ROWS <= head.y:
                break
            self.snake.insert(0, head)
            if head != self.food:
                self.snake.pop()
            else:
                self.gen_food()
            self.render()
        time.sleep(3)

    def gen_food(self):
        food = cords.Cords(random.randint(0, DISPLAY_COLUMNS - 1), random.randint(0, DISPLAY_ROWS - 1))
        if food in self.snake:
            self.gen_food()
        else:
            self.food = food

    def render(self):
        led.fill_func(self.render_func)

    def render_func(self, cord):
        if self.food == cord:
            return led.COLOR_RED
        elif cord in self.snake:
            return led.COLOR_GREEN
        return led.COLOR_BLACK
