class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if value in range(self.MIN_DIMENSION, self.MAX_DIMENSION + 1):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if value in range(self.MIN_DIMENSION, self.MAX_DIMENSION + 1):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if value in range(self.MIN_DIMENSION, self.MAX_DIMENSION + 1):
            self.__c = value

    def __ge__(self, other):
        if isinstance(other, Dimensions):
            return self.a * self.b * self.c >= other.a * other.b * other.c

    def __gt__(self, other):
        if isinstance(other, Dimensions):
            return self.a * self.b * self.c > other.a * other.b * other.c


class ShopItem:
    def __init__(self, name, price, dim):
        if isinstance(name, str):
            self.name = name
        if isinstance(price, (int, float)):
            self.price = price
        if isinstance(dim, Dimensions):
            self.dim = dim

    def __repr__(self):
        return f'Name = {self.name}, Volume = {self.dim.a * self.dim.b * self.dim.c / 10**9}'

it1 = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
it2 = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
it3 = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
it4 = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))

lst_shop = [it1, it2, it3, it4]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.a * x.dim.b * x.dim.a)
