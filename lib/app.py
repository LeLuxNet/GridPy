import time

from config import *
from lib import led, button


class BaseApp:

    def __init__(self, name):
        self.name = name

    def run(self):
        raise Exception('App not implemented')


class Player:

    def __init__(self, color, light_color=None):
        self.color = color
        self.light_color = light_color if light_color is not None else color

    def __eq__(self, other):
        if self is None or other is None:
            return False
        return self.color == other.color


red = Player(led.COLOR_RED, led.Color(255, 20, 20))
blue = Player(led.COLOR_BLUE, led.Color(10, 30, 255))

nobody = Player(led.COLOR_WHITE)


class GridGame(BaseApp):

    def __init__(self, name, line_len, width, height, sel_col=True, sel_row=True):
        super().__init__(name)
        self.width = width
        self.height = height
        self.game = []
        for x in range(width):
            col = []
            for y in range(height):
                col.append(None)
            self.game.append(col)
        self.sel_col = -1 if sel_col else -2
        self.sel_row = -1 if sel_row else -2
        self.line_len = line_len
        self.turn = red
        self.winner = None

    def run(self):
        while self.winner is None:
            if self.sel_col == -1:
                self.next_col()
                self.render()
                try:
                    while button.any_button()[0] == 0:
                        self.next_col()
                        self.render()
                except KeyboardInterrupt:
                    break
            if self.sel_row == -1:
                self.next_row()
                self.render()
                try:
                    while button.any_button()[0] == 0:
                        self.next_row()
                        self.render()
                except KeyboardInterrupt:
                    break

            self.drop()
            if self.turn == red:
                self.turn = blue
            else:
                self.turn = red
            if self.sel_col != -2:
                self.sel_col = -1
            if self.sel_row != -2:
                self.sel_row = -1
            self.winner = self.get_winner()
            self.render()

    def render(self):
        if self.winner is None:
            led.fill_func(self._render)
        else:
            led.fill(self.winner.color)
            time.sleep(1)
            led.clear()
            time.sleep(0.5)
            led.fill(self.winner.color)
            time.sleep(3)
            led.clear()

    def _render(self, cords):
        pass

    def drop(self):
        pass

    def get_winner(self):
        free = False
        for y in self.game:
            for x in y:
                if x is not None:
                    free = True
        if not free:
            return nobody

        # on x axis
        for x in range(self.width - self.line_len + 1):
            for y in range(self.height):
                if self.game[x][y] is None:
                    continue
                for i in range(1, self.line_len):
                    if self.game[x][y] != self.game[x + i][y]:
                        break
                else:
                    return self.game[x][y]

        # on y axis
        for x in range(self.width):
            for y in range(self.height - self.line_len + 1):
                if self.game[x][y] is None:
                    continue
                for i in range(1, self.line_len):
                    if self.game[x][y] != self.game[x][y + i]:
                        break
                else:
                    return self.game[x][y]

        # on / diagonal
        for x in range(self.width - self.line_len + 1):
            for y in range(self.line_len - 1, self.height):
                if self.game[x][y] is None:
                    continue
                for i in range(1, self.line_len):
                    if self.game[x][y] != self.game[x + i][y - i]:
                        break
                else:
                    return self.game[x][y]

        # on \ diagonal
        for x in range(self.width - self.line_len + 1):
            for y in range(self.height - self.line_len + 1):
                if self.game[x][y] is None:
                    continue
                for i in range(1, self.line_len):
                    if self.game[x][y] != self.game[x + i][y + i]:
                        break
                else:
                    return self.game[x][y]
        return None

    def next_col(self):
        self.sel_col += 1
        if self.sel_col >= self.width:
            self.sel_col = 0
        free = 0
        for y in range(self.height):
            if self.game[self.sel_col][y] is None:
                free += 1
                if self.sel_row != -2:
                    self.sel_row = y
        if free == 0:
            self.next_col()
        elif free != 1 and self.sel_row != -2:
            self.sel_row = -1

    def next_row(self):
        self.sel_row += 1
        if self.sel_row >= self.height:
            self.sel_row = 0
        if self.game[self.sel_col][self.sel_row] is not None:
            self.next_row()

    def calc_board(self):
        pixel_height = DISPLAY_ROWS // self.height
        pixel_width = DISPLAY_COLUMNS // self.width

        board_height = pixel_height * self.height
        board_width = pixel_width * self.width

        left_space = (DISPLAY_COLUMNS - board_width) // 2
        right_space = DISPLAY_COLUMNS - board_width - left_space
        top_space = (DISPLAY_ROWS - board_height) // 2
        bottom_space = DISPLAY_ROWS - board_height - top_space

        return [pixel_height, pixel_width,
                left_space, right_space, top_space, bottom_space]
