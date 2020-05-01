import random
import time
from datetime import datetime

import RPi.GPIO as GPIO
import neopixel

LED_COLUMNS = 10
LED_ROWS = 10

LED_REVERSED = True  # If every 2. row is in the opposite direction

LED_COUNT = LED_COLUMNS * LED_ROWS
LED_PIN = 18
LED_FREQ = 800000  # 800kHz
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

BUTTON_A_PIN = 19
BUTTON_B_PIN = 7
BUTTON_COOLDOWN = 150

MSPF = 20
FPS = 1000 / MSPF

SAVE = False

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


class Color:

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def toInt(self):
        return neopixel.Color(self.green, self.red, self.blue)  # Red and green are switched

    def toString(self):
        return str(self.red) + " " + str(self.green) + " " + str(self.blue)


class Button:

    def __init__(self, pin, cooldown):
        self.pin = pin
        self.cooldown = cooldown
        self.lastPress = datetime.now()
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def once(self):
        if GPIO.input(self.pin) == GPIO.HIGH:
            if (datetime.now() - self.lastPress).microseconds < self.cooldown * 1000:
                return False
            while True:
                if GPIO.input(self.pin) == GPIO.LOW:
                    self.lastPress = datetime.now()
                    return True
        return False

    def wait(self):
        while True:
            if self.once():
                return


def startSave(name):
    print("Start recording")
    global file
    file = open("matrix/" + name + ".txt", "w")
    global SAVE
    SAVE = True


def stopSave():
    print("Stop recording")
    global SAVE
    SAVE = False
    file.close()


def sleep(s):
    if SAVE:
        file.write("d" + str(s * 1000) + "\n")
    time.sleep(s)


def sleepMs(ms):
    if SAVE:
        file.write("d" + str(ms) + "\n")
    time.sleep(ms / 1000.0)


def isReversedRow(row):
    return LED_REVERSED and row % 2 == 1


def calcRow(i):
    return i / LED_COLUMNS


def calcColumn(i):
    if isReversedRow(calcRow(i)):
        return LED_COLUMNS - i % LED_COLUMNS - 1
    return i % LED_COLUMNS


def calcIndex(row, col):
    if row >= LED_ROWS or col >= LED_COLUMNS or row < 0 or col < 0:
        return LED_COUNT
    if isReversedRow(row):
        return (row + 1) * LED_COLUMNS - col - 1
    return row * LED_COLUMNS + col


def brightnessColor(brightness):
    return Color(brightness, brightness, brightness)


COLOR_TRANSPARENT = None
COLOR_BLACK = brightnessColor(0)

BG = COLOR_BLACK


def bBack():
    global BG
    BG = COLOR_BLACK


def tBack():
    global BG
    BG = COLOR_TRANSPARENT


COLOR_WHITE = brightnessColor(255)
COLOR_RED = Color(255, 0, 0)
COLOR_GREEN = Color(0, 255, 0)
COLOR_BLUE = Color(0, 0, 255)


def randomColor():
    return Color(random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255))


def mask(screen, mask, replace=Color(0, 0, 0)):
    for i in range(len(screen)):
        if not mask(screen, i):
            screen[i] = replace
    return screen


def functionScreen(func):
    result = []
    for i in range(strip.numPixels()):
        result.append(func(i))
    return result


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


def oneColorScreen(color=BG):
    result = []
    for i in range(strip.numPixels()):
        result.append(color)
    return result


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


def toScreen(map, x=0, y=0):
    screen = oneColorScreen()
    for mx in range(len(map)):
        for my in range(len(map[mx])):
            index = calcIndex(x + mx, y + my)
            if index == LED_COUNT:
                continue
            screen[index] = map[mx][my]
    return screen


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


def button():
    while True:
        if buttonA.once():
            return 0
        if buttonB.once():
            return 1


def buttonA():
    buttonA.wait()


def buttonB():
    buttonB.wait()


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


def clear():
    applyScreen(oneColorScreen(COLOR_BLACK))


def init():
    GPIO.setmode(GPIO.BOARD)

    global buttonA
    global buttonB
    buttonA = Button(BUTTON_A_PIN, BUTTON_COOLDOWN)
    buttonB = Button(BUTTON_B_PIN, BUTTON_COOLDOWN)

    global strip
    strip = neopixel.Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    global currentScreen
    currentScreen = oneColorScreen(COLOR_BLACK)
    print("FPS: " + str(FPS))
    print("MsPF: " + str(MSPF))
    print("")
    print("Start matrix")
