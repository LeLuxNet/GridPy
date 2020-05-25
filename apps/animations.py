import animations
from lib import app, colors, button
from utils import time


class App(app.BaseApp):

    def __init__(self):
        super().__init__("Animations")
        self.detector = button.QuitDetector()

    def run(self):
        try:
            self.detector.start()

            animations.diagonal_random()
            self.detector.check()

            time.sleep(1)
            self.detector.check()

            for i in range(5):
                animations.snake(colors.random_color(), i % 2 == 0)
                self.detector.check()

            animations.pixel_glitter_random()
            self.detector.check()
        except KeyboardInterrupt:
            return
