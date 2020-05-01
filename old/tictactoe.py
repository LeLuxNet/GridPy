from old.matrix import *

turn = 1
winner = 0

selRow = -1
selCol = -1

game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def render():
  if winner == 0:
    screen = functionScreen(renderFunc)
    applyScreen(screen)
  else:
    if winner == 1:
      color = COLOR_RED
    elif winner == 2:
      color = COLOR_BLUE
    else:
      color = COLOR_WHITE
    screen = oneColorScreen(color)
    applyScreen(screen)
    sleep(1)
    applyScreen(oneColorScreen(COLOR_BLACK))
    sleepMs(500)
    applyScreen(screen)

def renderFunc(i):
  x = toGameCords(calcColumn(i))
  y = toGameCords(calcRow(i))
  if x == -1 or y == -1:
    if turn == 1:
      return COLOR_RED
    else:
      return COLOR_BLUE
  elif game[x][y] == 1:
    return COLOR_RED
  elif game[x][y] == 2:
    return COLOR_BLUE
  elif (selCol == x and selRow == -1) or (selCol == x and selRow == y):
    return COLOR_WHITE
  return COLOR_BLACK

def toGameCords(val):
  if val <= 2:
    return 0
  elif val >= 3 and val <= 5:
    return 1
  elif val >= 6 and val <= 8:
    return 2
  return -1

def hasWinner():
  if winnerCol(0):
    return game[0][0]
  elif winnerCol(1):
    return game[1][0]
  elif winnerCol(2):
    return game[2][0]
  elif winnerRow(0):
    return game[0][0]
  elif winnerRow(1):
    return game[0][1]
  elif winnerRow(2):
    return game[0][2]
  elif game[0][0] == game[1][1] == game[2][2]:
    return game[0][0]
  elif game[0][2] == game[1][1] == game[2][0]:
    return game[0][2]
  free = False
  for x in game:
    for y in x:
      if y == 0:
        free = True
        break
  if not free:
    return 3
  return 0

def winnerCol(i):
  return game[i][0] == game[i][1] == game[i][2]

def winnerRow(i):
  return game[0][i] == game[1][i] == game[2][i]

def plusCol():
  global selCol
  selCol += 1
  if selCol > 2:
    selCol = 0
  if game[selCol][0] != 0 and game[selCol][1] != 0 and game[selCol][2] != 0:
    plusCol()

def plusRow():
  global selRow
  selRow += 1
  if selRow > 2:
    selRow = 0
  if game[selCol][selRow] != 0:
    plusRow()

init()

while winner == 0:
  plusCol()
  render()
  while button() == 0:
    plusCol()
    render()
  free = 0
  freePos = -1
  for y in range(3):
    if game[selCol][y] == 0:
      free += 1
      freePos = y
  if free == 1:
    selRow = freePos
  else:
    plusRow()
    render()
    while button() == 0:
      plusRow()
      render()
  x = selCol
  y = selRow
  selCol = -1
  selRow = -1
  if x >= len(game) or y >= len(game[x]):
    continue
  if game[x][y] != 0:
    continue
  game[x][y] = turn
  if turn == 1:
    turn = 2
  else:
    turn = 1
  winner = hasWinner()
render()
sleep(3)

quit()
