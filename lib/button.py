import datetime

import RPi.GPIO as GPIO

from config import *


class Button:

    def __init__(self, pin):
        self.pin = pin
        self.last_press = datetime.datetime.now()
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        buttons.append(self)

    def once(self):
        if GPIO.input(self.pin) == GPIO.HIGH:
            if (datetime.datetime.now() - self.last_press).microseconds < BUTTON_COOLDOWN * 1000:
                return False
            down_time = datetime.datetime.now()
            while True:
                if GPIO.input(self.pin) == GPIO.LOW:
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


def any_button():
    while True:
        for i in range(len(buttons)):
            result = buttons[i].once()
            if result:
                return [i, result]


def cleanup():
    GPIO.cleanup()


GPIO.setmode(GPIO.BCM)

buttons = []
buttonA = Button(BUTTON_A_PIN)
buttonB = Button(BUTTON_B_PIN)
