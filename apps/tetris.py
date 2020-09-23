import collections
import datetime
import random

from config import *
from lib import app, led, button
from lib.colors import COLOR_BLACK, COLOR_CYAN, COLOR_RED, COLOR_BLUE, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, \
    COLOR_MAGENTA
from lib.cords import Cords
from utils import time

Shape = collections.namedtuple('Shape', 'color pos pivot')

SHAPES = [
    Shape(COLOR_CYAN, [(0, 0), (0, 1), (0, 2), (0, 3)], (1.5, 1.5)),
    Shape(COLOR_BLUE, [(0, 0), (0, 1), (1, 1), (2, 1)], (1, 1)),
    Shape(COLOR_ORANGE, [(0, 1), (1, 1), (2, 1), (2, 0)], (1, 1)),
    Shape(COLOR_YELLOW, [(0, 0), (0, 1), (1, 0), (1, 1)], (0.5, 0.5)),
    Shape(COLOR_GREEN, [(0, 1), (1, 1), (1, 0), (2, 0)], (1, 1)),
    Shape(COLOR_MAGENTA, [(1, 0), (0, 1), (1, 1), (2, 1)], (1, 1)),
    Shape(COLOR_RED, [(0, 0), (1, 0), (1, 1), (2, 1)], (1, 1))
]

SPEED = 900


class Block:

    def __init__(self, shape):
        self.color = shape.color

        middle = DISPLAY_COLUMNS // 2 - int(shape.pivot[0])
        self.pos = list(map(lambda x: Cords(x[0] + middle, x[1]), shape.pos))
        self.pivot = Cords(shape.pivot[0] + middle, shape.pivot[1])


class App(app.BaseApp):

    def __init__(self):
        super().__init__("Tetris")
        self.running = True
        self.game = app.generate_grid(DISPLAY_COLUMNS, DISPLAY_ROWS)

        self.falling = None
        self.gen_falling()

    def run(self):
        self.render()
        while self.running:
            begin = datetime.datetime.now()
            try:
                while time.to_ms(datetime.datetime.now() - begin) < SPEED:
                    press = button.any_button_once()

                    if press is not None:
                        if press[1] == 1:
                            self.move(-1 if press[0] == 0 else 1)
                        elif press[1] == 2 and press[0] == 1:
                            self.rotate()
            except KeyboardInterrupt:
                break

            self.down()

        time.sleep(3)

    def gen_falling(self):
        self.falling = Block(random.choice(SHAPES))

        for cord in self.falling.pos:
            if self.game[cord.x][cord.y] is not None:
                self.running = False
                self.render()
                return

    def move(self, direction):
        for cord in self.falling.pos:
            x = cord.x + direction
            if x < 0 or x >= len(self.game) or self.game[x][cord.y] is not None:
                return

        for cord in self.falling.pos:
            cord.x += direction
        self.falling.pivot.x += direction
        self.render()

    def rotate(self):
        for cord in self.falling.pos:
            x = self.falling.pivot.y + self.falling.pivot.x - cord.y
            if x < 0 or x >= len(self.game):
                return

            y = self.falling.pivot.y - self.falling.pivot.x + cord.x
            if y < 0 or y >= len(self.game[0]):
                return

        for cord in self.falling.pos:
            old_x = cord.x
            cord.x = int(self.falling.pivot.y + self.falling.pivot.x) - cord.y
            cord.y = int(self.falling.pivot.y - self.falling.pivot.x) + old_x
        self.render()

    def down(self):
        for cord in self.falling.pos:
            y = cord.y + 1
            if y >= len(self.game) or self.game[cord.x][y] is not None:
                self.lay_down()
                return

        for cord in self.falling.pos:
            cord.y += 1
        self.falling.pivot.y += 1
        self.render()

    def lay_down(self):
        for cord in self.falling.pos:
            self.game[cord.x][cord.y] = self.falling.color

        for i in range(len(self.game[0])):
            for col in self.game:
                if col[i] is None:
                    break
            else:
                for col in self.game:
                    col.pop(i)
                    col.insert(0, None)

        self.gen_falling()
        self.render()

    def render(self):
        led.fill_func(self.render_func)

    def render_func(self, cord):
        if cord in self.falling.pos:
            return self.falling.color

        block = self.game[cord.x][cord.y]
        if block is None:
            return COLOR_BLACK
        return block
