from lib import app, led


class App(app.GridGame):

    def __init__(self):
        super().__init__("TicTacToe", 3, 3, 3)
        self.board = self.calc_board()

    def _render(self, cords):
        x = (cords.x - self.board[2]) // self.board[1]
        y = (cords.y - self.board[4]) // self.board[0]
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return self.turn.light_color
        elif self.game[x][y] is not None:
            return self.game[x][y].color
        elif self.sel_col == x and (self.sel_row == -1 or self.sel_row == y):
            return led.COLOR_WHITE
        return led.COLOR_BLACK

    def drop(self):
        self.game[self.sel_col][self.sel_row] = self.turn
