from animations.color import base


class ListGenerator(base.ColorGeneration):

    def __init__(self, colors):
        self.colors = colors
        self.index = 0

    def generate(self):
        color = self.colors[self.index]
        self.index += 1
        if self.index >= len(self.colors):
            self.index = 0
        return color
