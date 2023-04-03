class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __check_num_int_float(self, num):
        return True if type(num) in (int, float) else False

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if not self.__check_num_int_float(value):
            raise ValueError("Неверный тип данных.")
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if not self.__check_num_int_float(value):
            raise ValueError("Неверный тип данных.")
        self.__img = value

    def __abs__(self):
        return (self.__real * self.__real + self.__img * self.__img) ** 0.5


cmp = Complex(7, 8)
cmp.real, cmp.img = 3, 4
c_abs = abs(cmp)
