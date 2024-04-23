class Color:
    def __int__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color