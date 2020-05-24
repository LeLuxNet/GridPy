from lib import app, led


class App(app.BaseApp):

    def __init__(self):
        super().__init__("Animations")

    def run(self):
        led.clear()
