from animations import coded
from animations.color import DifferentRandomGeneration, RainbowGeneration
from config import *
from lib import app, button, cords
from utils import time

GEN = DifferentRandomGeneration(100)


class App(app.BaseApp):

    def __init__(self):
        super().__init__("Animations")
        self.detector = button.QuitDetector()

    def run(self):
        self.detector.start()
        try:
            while True:
                rainbow = RainbowGeneration((DISPLAY_ROWS + DISPLAY_COLUMNS) * 2)
                for i in [cords.TOP, cords.LEFT, cords.BOTTOM, cords.RIGHT]:
                    coded.lines(rainbow, i)
                    self.detector.check()

                coded.spiral_zoom(GEN, 10)
                self.detector.check()

                for i in [cords.TOP_LEFT, cords.TOP_RIGHT, cords.BOTTOM_RIGHT, cords.BOTTOM_LEFT]:
                    coded.diagonal(GEN, i)
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
