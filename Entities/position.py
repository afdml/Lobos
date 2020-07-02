class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # region getters
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    # endregion

    # region setters
    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    # endregion

    # region Move Functions
    def moveN(self, land):
        return Position(self.x % land.tamX, self.y + 1 % land.tamY)

    def moveNE(self, land):
        return Position(self.x + 1 % land.tamX, self.y + 1 % land.tamY)

    def moveE(self, land):
        return Position(self.x + 1 % land.tamX, self.y % land.tamY)

    def moveES(self, land):
        return Position(self.x + 1 % land.tamX, self.y - 1 % land.tamY)

    def moveS(self, land):
        return Position(self.x % land.tamX, self.y - 1 % land.tamY)

    def moveSO(self, land):
        return Position(self.x - 1 % land.tamX, self.y - 1 % land.tamY)

    def moveO(self, land):
        return Position(self.x - 1 % land.tamX, self.y % land.tamY)

    def moveON(self, land):
        return Position(self.x - 1 % land.tamX, self.y + 1 % land.tamY)
    # endregion