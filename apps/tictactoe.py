import time

from lib import led, button


class Player:

    def __init__(self, color):
        self.color = color


red = Player(led.COLOR_RED)
blue = Player(led.COLOR_BLUE)

nobody = Player(led.COLOR_WHITE)

turn = red
winner = None

game = [[None, None, None],
        [None, None, None],
        [None, None, None]]

selCol = -1
selRow = -1


def render():
    if winner is None:
        led.fill_func(_render_ingame)
        pass
    else:
        led.fill(winner.color)
        time.sleep(1)
        led.clear()
        time.sleep(0.5)
        led.fill(winner.color)
        time.sleep(3)
        led.clear()


def _render_ingame(cords):
    x = calc_game_pos(cords.x)
    y = calc_game_pos(cords.y)
    if x == -1 or y == -1:
        return turn.color
    elif game[x][y] is not None:
        return game[x][y].color
    elif selCol == x and (selRow == -1 or selRow == y):
        return led.COLOR_WHITE
    return led.COLOR_BLACK


def calc_game_pos(val):
    if val <= 2:
        return 0
    elif 3 <= val <= 5:
        return 1
    elif 6 <= val <= 8:
        return 2
    return -1


def get_winner():
    for y in game:
        if y[0] == y[1] == y[2]:
            return y[0]
    for x in range(3):
        if game[0][x] == game[1][x] == game[2][x]:
            return game[0][x]
    if game[0][0] == game[1][1] == game[2][2]:
        return game[0][0]
    if game[0][2] == game[1][1] == game[2][0]:
        return game[0][2]
    free = False
    for y in game:
        for x in y:
            if x is None:
                free = True
                break
    if not free:
        return nobody
    return None


def next_col():
    global selCol
    selCol += 1
    if selCol > 2:
        selCol = 0
    if game[selCol][0] is not None and \
            game[selCol][1] is not None and \
            game[selCol][2] is not None:
        next_col()


def next_row():
    global selRow
    selRow += 1
    if selRow > 2:
        selRow = 0
    if game[selCol][selRow] is not None:
        next_row()


while winner is None:
    next_col()
    render()
    while button.any_button()[0] == 0:
        next_col()
        render()
    free_count = 0
    free_pos = -1
    for y in range(3):
        if game[selCol][y] is None:
            free_count += 1
            free_pos = y
    if free_count == 1:
        selRow = free_pos
    else:
        next_row()
        render()
        while button.any_button()[0] == 0:
            next_row()
            render()
    game[selCol][selRow] = turn
    selCol = -1
    selRow = -1
    if turn == red:
        turn = blue
    else:
        turn = red
    winner = get_winner()
render()
