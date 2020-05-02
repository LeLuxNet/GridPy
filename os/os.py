import importlib
from time import sleep

from lib import button, led

view = 2


def _init():
    led.show_image("assets/logo.png")
    sleep(2)
    led.clear()


def _quit():
    button.cleanup()


def run():
    if view == 0:
        # App Drawer
        pass
    elif view == 1:
        # Animations
        pass
    elif view == 2:
        start_app("tictactoe")


def start_app(name):
    importlib.import_module("apps." + name)
    global view
    view = 1


_init()

while True:
    run()

_quit()
