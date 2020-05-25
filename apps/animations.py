from animations import coded
from animations.color import random
from lib import app, button
from utils import time

GEN = random


class App(app.BaseApp):

    def __init__(self):
        super().__init__("Animations")
        self.detector = button.QuitDetector()

    def run(self):
        self.detector.start()
        try:
            while True:
                coded.spiral_zoom(GEN, 10)
                self.detector.check()

                coded.diagonal(GEN)
                self.detector.check()

                time.sleep(1)
                self.detector.check()

                for i in range(3):
                    coded.snake(GEN, i % 2 == 0)
                    self.detector.check()

                coded.pixel_glitter(GEN)
                self.detector.check()
        except KeyboardInterrupt:
            return
