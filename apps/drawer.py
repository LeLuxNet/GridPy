from config import *
from lib import app, char, button, led
from system import view, main


class App(app.BaseApp):

    def __init__(self):
        super().__init__("Drawer")
        self.sel = 1

    def run(self):
        led.clear()
        while True:
            app = view.get_app(main.apps[self.sel])
            char.gliding_text(app.name, DISPLAY_ROWS - 5, fade_out=True, fade_in=True)
            press = button.any_button(False)
            if press[0] == 0:
                self.sel += 1
                if self.sel >= len(main.apps):
                    self.sel = 1
            elif press[0] == 1:
                view.next_view(self.sel + 1)
                break
