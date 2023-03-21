class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x1=0, y1=0):
        self.__x = self.__y = 0
        self.x = x1
        self.y = y1

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) in (int, float) and RadiusVector2D.MIN_COORD <= value <= RadiusVector2D.MAX_COORD:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) in (int, float) and RadiusVector2D.MIN_COORD <= value <= RadiusVector2D.MAX_COORD:
            self.__y = value

    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y
