from time import sleep

from api import api
from lib import led, button
from system import main


def init():
    led.show_image("assets/logo.png")
    button.init()
    api.run()
    sleep(2)
    led.clear()


init()
while True:
    main.run()
