import datetime

import RPi.GPIO as GPIO

A_PIN = 7
B_PIN = 11

COOLDOWN = 150  # Cooldown in ms


class Button:

    def __init__(self, pin):
        self.pin = pin
        self.last_press = datetime.datetime.now()
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def once(self):
        if GPIO.input(self.pin) == GPIO.HIGH:
            if (datetime.datetime.now() - self.last_press).microseconds < COOLDOWN * 1000:
                return False
            while True:
                if GPIO.input(self.pin) == GPIO.LOW:
                    self.last_press = datetime.datetime.now()
                    return True
        return False

    def wait(self):
        while True:
            if self.once():
                return


def any_button():
    while True:
        if buttonA.once():
            return 0
        if buttonB.once():
            return 1


def cleanup():
    GPIO.cleanup()


GPIO.setmode(GPIO.BOARD)

buttonA = Button(A_PIN)
buttonB = Button(B_PIN)
