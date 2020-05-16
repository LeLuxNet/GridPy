import time

from lib import led, button, app


class Player:

    def __init__(self, color):
        self.color = color


red = Player(led.COLOR_RED)
blue = Player(led.COLOR_BLUE)

nobody = Player(led.COLOR_WHITE)


def calc_game_pos(val):
    if val <= 2:
        return 0
    elif 3 <= val <= 5:
        return 1
    elif 6 <= val <= 8:
        return 2
    return -1


class App(app.BaseApp):

    def __init__(self):
        super().__init__("TicTacToe")
        self.turn = red
        self.winner = None

        self.game = [[None, None, None],
                     [None, None, None],
                     [None, None, None]]

        self.selCol = -1
        self.selRow = -1

    def render(self):
        if self.winner is None:
            led.fill_func(self._render_ingame)
            pass
        else:
            led.fill(self.winner.color)
            time.sleep(1)
            led.clear()
            time.sleep(0.5)
            led.fill(self.winner.color)
            time.sleep(3)
            led.clear()

    def _render_ingame(self, cords):
        x = calc_game_pos(cords.x)
        y = calc_game_pos(cords.y)
        if x == -1 or y == -1:
            return self.turn.color
        elif self.game[x][y] is not None:
            return self.game[x][y].color
        elif self.selCol == x and (self.selRow == -1 or self.selRow == y):
            return led.COLOR_WHITE
        return led.COLOR_BLACK

    def get_winner(self):
        for y in self.game:
            if y[0] == y[1] == y[2]:
                return y[0]
        for x in range(3):
            if self.game[0][x] == self.game[1][x] == self.game[2][x]:
                return self.game[0][x]
        if self.game[0][0] == self.game[1][1] == self.game[2][2]:
            return self.game[0][0]
        if self.game[0][2] == self.game[1][1] == self.game[2][0]:
            return self.game[0][2]
        free = False
        for y in self.game:
            for x in y:
                if x is None:
                    free = True
                    break
        if not free:
            return nobody
        return None

    def next_col(self):
        self.selCol += 1
        if self.selCol > 2:
            self.selCol = 0
        if self.game[self.selCol][0] is not None and \
                self.game[self.selCol][1] is not None and \
                self.game[self.selCol][2] is not None:
            self.next_col()

    def next_row(self):
        self.selRow += 1
        if self.selRow > 2:
            self.selRow = 0
        if self.game[self.selCol][self.selRow] is not None:
            self.next_row()

    def run(self):
        while self.winner is None:
            self.next_col()
            self.render()
            try:
                while button.any_button(True)[0] == 0:
                    self.next_col()
                    self.render()
            except KeyboardInterrupt:
                break
            free_count = 0
            free_pos = -1
            for y in range(3):
                if self.game[self.selCol][y] is None:
                    free_count += 1
                    free_pos = y
            if free_count == 1:
                self.selRow = free_pos
            else:
                self.next_row()
                self.render()
                try:
                    while button.any_button(True)[0] == 0:
                        self.next_row()
                        self.render()
                except KeyboardInterrupt:
                    break
            self.game[self.selCol][self.selRow] = self.turn
            self.selCol = -1
            self.selRow = -1
            if self.turn == red:
                self.turn = blue
            else:
                self.turn = red
            self.winner = self.get_winner()
        self.render()
