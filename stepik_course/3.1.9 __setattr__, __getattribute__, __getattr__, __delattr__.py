class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    attrs = {'a': (int, float), 'b': (int, float), 'c': (int, float)}

    def __init__(self, a, b, c):
        self.__a = self.__b = self.__c = 10
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        if key in self.attrs and type(value) not in self.attrs[key]:
            return
        if value < self.MIN_DIMENSION or value > self.MAX_DIMENSION:
            return

        super().__setattr__(key, value)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value
