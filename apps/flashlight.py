from lib import led, button, app
from lib.colors import *


class App(app.BaseApp):

    def __init__(self):
        super().__init__("Flashlight")
        self.color = COLOR_WHITE
        self.brightness = BRIGHTNESS_NORMAL

    def run(self):
        while True:
            led.fill(Color(self.color.red, self.color.green, self.color.blue, self.brightness))
            try:
                press = button.any_button()
            except KeyboardInterrupt:
                break
            if press[0] == 0:
                self.next_color()
            elif press[0] == 1:
                self.next_brightness()

    def next_color(self):
        if self.color == COLOR_WHITE:
            self.color = COLOR_WHITE_WARM
        else:
            self.color = COLOR_WHITE

    def next_brightness(self):
        if self.brightness == BRIGHTNESS_NORMAL:
            self.brightness = BRIGHTNESS_HIGH
        elif self.brightness == BRIGHTNESS_HIGH:
            self.brightness = BRIGHTNESS_LOW
        else:
            self.brightness = BRIGHTNESS_NORMAL
