from lib import app, led, button


class App(app.BaseApp):

    def __init__(self):
        super().__init__("Test card")

    def run(self):
        led.show_image("assets/test_card.png")
        while button.any_button(False) != [0, 2]:
            pass
