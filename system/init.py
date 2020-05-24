import signal
import time
import traceback
from time import sleep

from api import api
from lib import led, button
from system import main


def init():
    signal.signal(signal.SIGINT, _on_signal)
    signal.signal(signal.SIGTERM, _on_signal)

    led.show_image("assets/logo.png")
    button.init()
    api.run()
    sleep(2)
    led.clear()


def _on_signal(signum, frame):
    quit()


def quit():
    button.cleanup()
    led.clear()


init()
try:
    while True:
        main.run()
except:
    print(traceback.format_exc())
    led.fill_func(lambda cord: led.COLOR_RED if cord.y % 2 == 0 else led.COLOR_YELLOW)
    time.sleep(5)
    quit()
