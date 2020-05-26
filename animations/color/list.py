from animations.color import base


class ListGenerator(base.IndexColorGeneration):

    def __init__(self, colors):
        super().__init__(len(colors))
        self.colors = colors

    def generate_index(self, index):
        return self.colors[index]
