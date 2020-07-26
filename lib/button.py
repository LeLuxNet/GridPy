import datetime
from threading import Thread

from config import *
from hardware import button_lib
from utils import time


class Button:

    def __init__(self, pin):
        self.pin = pin
        self.last_press = datetime.datetime.now()
        button_lib.setup(pin)
        buttons.append(self)
        self.id = len(buttons) - 1
        self.vpress = None

    def once(self):
        if self.vpress:
            length = self.vpress
            self.vpress = None
            return length
        if button_lib.pressed(self):
            if time.to_ms(datetime.datetime.now() - self.last_press) < BUTTON_COOLDOWN:
                return False
            down_time = datetime.datetime.now()
            while True:
                if not button_lib.pressed(self):
                    self.last_press = datetime.datetime.now()
                    if (self.last_press - down_time).microseconds > BUTTON_LONG_PRESS * 1000:
                        return 2
                    else:
                        return 1
        return False

    def wait(self):
        while True:
            result = self.once()
            if result:
                return result

    def press(self, length=1):
        self.vpress = length


def any_button(throw=True):
    while True:
        press = any_button_once(throw)
        if press:
            return press


def any_button_once(throw=True):
    for i, button in enumerate(buttons):
        result = button.once()
        if result:
            print("Button:", i, result)
            if throw and i == 0 and result == 2:
                raise KeyboardInterrupt()
            return [i, result]


buttons = []


def init():
    Button(BUTTON_A_PIN)
    Button(BUTTON_B_PIN)


class QuitDetector(Thread):

    def __init__(self, throw=True):
        super().__init__()
        self.stop = False
        self.throw = throw

    def run(self):
        try:
            while True:
                any_button(True)
        except KeyboardInterrupt:
            self.stop = True

    def check(self):
        if self.throw and self.stop:
            raise KeyboardInterrupt
        return self.stop
