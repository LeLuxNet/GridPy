from config import *
from lib import app, led


class App(app.GridGame):

    def __init__(self):
        super().__init__("Connect Four", 4, DISPLAY_COLUMNS, DISPLAY_ROWS - 1, sel_row=False)

    def _render(self, cords):
        if cords.y == 0:
            if self.sel_col == cords.x:
                return self.turn.light_color
        else:
            field = self.game[cords.x][cords.y - 1]
            if field is not None:
                return field.color
        return led.COLOR_BLACK

    def drop(self):
        for i in range(len(self.game[self.sel_col]) - 1, -1, -1):
            if self.game[self.sel_col][i] is None:
                self.game[self.sel_col][i] = self.turn
                break
