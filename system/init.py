import signal
import time
import traceback
from time import sleep

from hardware import button_lib
from lib import led, button
from system import main


def init():
    print("Init")
    led.show_image("assets/logo.png")

    signal.signal(signal.SIGINT, _on_signal)
    signal.signal(signal.SIGTERM, _on_signal)

    button.init()

    import api
    api.run()

    sleep(2)

    led.clear()


def _on_signal(_, __):
    stop()


def stop():
    print("Quit")
    button_lib.cleanup()
    led.clear()


if __name__ == "__main__":
    init()
    try:
        while True:
            main.run()
    except:
        print(traceback.format_exc())
        led.fill_func(lambda cord: led.COLOR_RED if cord.y % 2 == 0 else led.COLOR_YELLOW)
        time.sleep(5)
        stop()
