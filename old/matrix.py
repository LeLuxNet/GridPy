import random
import time

import neopixel

CHARS = {
    "A": [[0, 1, 0], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]],
    "B": [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 1], [1, 1, 0]],
    "C": [[1, 1, 1], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 1]],
    "D": [[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 0]],
    "E": [[1, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 0], [1, 1, 1]],
    "F": [[1, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 0], [1, 0, 0]],
    "G": [[1, 1, 1], [1, 0, 0], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
    "H": [[1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 0, 1]],
    "I": [[1], [1], [1], [1], [1]],
    "J": [[0, 0, 1], [0, 0, 1], [0, 0, 1], [1, 0, 1], [0, 1, 0]],
    "K": [[1, 0, 1], [1, 1, 0], [1, 0, 0], [1, 1, 0], [1, 0, 1]],
    "L": [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 1]],
    "M": [[1, 0, 0, 0, 1], [1, 1, 0, 1, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1]],
    "N": [[1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 1]],
    "O": [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
    "P": [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 0], [1, 0, 0]],
    "Q": [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1]],
    "R": [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 1, 0], [1, 0, 1]],
    "S": [[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
    "T": [[1, 1, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
    "U": [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
    "V": [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0]],
    "W": [[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 1, 0, 1, 1], [1, 0, 0, 0, 1]],
    "x": [[0, 0, 0], [0, 0, 0], [1, 0, 1], [0, 1, 0], [1, 0, 1]],
    "X": [[1, 0, 1], [1, 0, 1], [0, 1, 0], [1, 0, 1], [1, 0, 1]],
    "Y": [[1, 0, 1], [1, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0]],
    "Z": [[1, 1, 1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]],
    "0": [[0, 1, 0], [1, 0, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0]],
    "1": [[0, 1], [1, 1], [0, 1], [0, 1], [0, 1]],
    " ": [[0], [0], [0], [0], [0]]
}

def sleepMs(ms):
    if SAVE:
        file.write("d" + str(ms) + "\n")
    time.sleep(ms / 1000.0)


def brightnessColor(brightness):
    return Color(brightness, brightness, brightness)


COLOR_TRANSPARENT = None

BG = COLOR_BLACK


def bBack():
    global BG
    BG = COLOR_BLACK


def tBack():
    global BG
    BG = COLOR_TRANSPARENT

def mask(screen, mask, replace=Color(0, 0, 0)):
    for i in range(len(screen)):
        if not mask(screen, i):
            screen[i] = replace
    return screen

def applyScreen(screen):
    global currentScreen
    new = False
    for i in range(strip.numPixels()):
        if screen[i] != COLOR_TRANSPARENT:
            strip.setPixelColor(i, screen[i].toInt())
            if SAVE and currentScreen[i].toString() != screen[i].toString():
                file.write("c" + str(i) + " " + str(screen[i].toInt()) + "\n")
                new = True
    if new:
        file.write("s\n")
    strip.show()
    currentScreen = screen[:]


def rowSnake(screen, back=None):
    frames = []
    if back == None:
        back = oneColorScreen(COLOR_BLACK)
    for i in range(strip.numPixels()):
        if not LED_REVERSED and calcRow(i) % 2 == 1:
            back[calcIndex(calcRow(i), LED_COLUMNS - calcColumn(i))] = screen[i]
        else:
            back[i] = screen[i]
        frames.append(back[:])
    return frames

def pixelScreen(i, color, screen=None):
    if screen == None:
        screen = oneColorScreen(COLOR_BLACK)
    screen[i] = color
    return screen


def gradientScreen(color1, color2):
    result = []
    for i in range(strip.numPixels()):
        result.append(interpolateColor(color1, color2, i, strip.numPixels()))
    return result


def colorize(map, color=COLOR_WHITE):
    colored = []
    for mx in range(len(map)):
        layer = []
        for my in range(len(map[mx])):
            if map[mx][my] == 1:
                layer.append(color)
            else:
                layer.append(BG)
        colored.append(layer)
    return colored


def runScreens(screens, delay=MSPF):
    for s in screens:
        applyScreen(s)
        sleepMs(delay)


def interpolateVal(val1, val2, frame, frameCount):
    return int(((val1 * (1 - frame / float(frameCount))) + (val2 * (frame / float(frameCount)))) / 2)


def interpolateColor(color1, color2, frame, frameCount):
    return Color(interpolateVal(color1.red, color2.red, frame, frameCount),
                 interpolateVal(color1.green, color2.green, frame, frameCount),
                 interpolateVal(color1.blue, color2.blue, frame, frameCount))


def interpolateBetween(screen1, screen2, s=1):
    result = []
    frames = s * FPS
    for f in range(frames):
        screen = []
        for i in range(len(screen1)):
            screen.append(interpolateColor(screen1[i], screen2[i], f, frames - 1))
        result.append(screen)
    return result


def quit():
    print("Stop matrix")
    clear()


def getChar(char, color=COLOR_WHITE):
    if char in CHARS:
        return colorize(CHARS[char], color)
    else:
        return colorize(CHARS[char.upper()], color)


def getString(string, color=COLOR_WHITE):
    first = True
    map = [[], [], [], [], []]
    for c in string:
        char = getChar(c, color)
        for row in range(len(map)):
            if not first:
                map[row].append(BG)
            for val in char[row]:
                map[row].append(val)
        first = False
    return map
