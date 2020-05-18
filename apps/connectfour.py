import time

from config import *
from lib import app, led, button


class Player:

    def __init__(self, color):
        self.color = color


red = Player(led.COLOR_RED)
blue = Player(led.COLOR_BLUE)


class App(app.BaseApp):

    def __init__(self):
        super().__init__("Connect Four")
        self.game = []
        for x in range(LED_COLUMNS):
            col = []
            for y in range(LED_ROWS - 1):
                col.append(None)
            self.game.append(col)
        self.selCol = 0
        self.turn = red
        self.winner = None

    def run(self):
        self.render()
        while True:
            try:
                while button.any_button()[0] == 0:
                    self.next_col()
                    self.render()
            except KeyboardInterrupt:
                break
            self.drop()
            if self.turn == red:
                self.turn = blue
            else:
                self.turn = red
            self.selCol = -1
            self.next_col()
            self.winner = self.get_winner()
            self.render()

    def render(self):
        if self.winner is None:
            led.fill_func(self._render_ingame)
        else:
            led.fill(self.winner.color)
            time.sleep(1)
            led.clear()
            time.sleep(0.5)
            led.fill(self.winner.color)
            time.sleep(3)
            led.clear()

    def _render_ingame(self, pos):
        if pos.y == 0:
            if self.selCol == pos.x:
                return self.turn.color
        else:
            field = self.game[pos.x][pos.y - 1]
            if field is not None:
                return field.color
        return led.COLOR_BLACK

    def next_col(self):
        self.selCol += 1
        if self.selCol >= LED_COLUMNS:
            self.selCol = 0
        for i in self.game[self.selCol]:
            if i is None:
                return
        self.nextCol()

    def drop(self):
        for i in range(len(self.game[self.selCol]) - 1, -1, -1):
            if self.game[self.selCol][i] is None:
                self.game[self.selCol][i] = self.turn
                break

    def get_winner(self):
        for x in self.game:
            player = None
            count = 0
            for y in x:
                if y is None:
                    continue
                if player == y:
                    count += 1
                else:
                    player = y
                    count = 1
                if count == 4:
                    return player
        for y in range(len(self.game[0])):
            player = None
            count = 0
            for x in range(len(self.game)):
                if self.game[x][y] is None:
                    continue
                if player == self.game[x][y]:
                    count += 1
                else:
                    player = self.game[x][y]
                    count = 1
                if count == 4:
                    return player
        return None
