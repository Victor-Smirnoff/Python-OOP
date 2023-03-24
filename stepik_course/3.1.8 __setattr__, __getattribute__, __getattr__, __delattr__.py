class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def __getattr__(self, item):
        return False

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            super().__setattr__(key, value)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self.__radius = value
