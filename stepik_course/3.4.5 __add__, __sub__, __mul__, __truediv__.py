class ListMath:
    def __init__(self, lst=None):
        self.lst_math = [x for x in lst if self.__check_type_other(x)] if lst and type(lst) == list else []

    def get_lst_math(self):
        return self.lst_math

    @staticmethod
    def __check_type_other(other):
        return type(other) in (int, float)

    def __add__(self, other):
        if not self.__check_type_other(other):
            raise ArithmeticError('значение должно быть int или float')

        return ListMath([x + other for x in self.lst_math])

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if not self.__check_type_other(other):
            raise ArithmeticError('значение должно быть int или float')

        self.lst_math = [x + other for x in self.lst_math]
        return self

    def __sub__(self, other):
        if not self.__check_type_other(other):
            raise ArithmeticError('значение должно быть int или float')

        return ListMath([x - other for x in self.lst_math])

    def __rsub__(self, other):
        return ListMath([other - x for x in self.lst_math])

    def __isub__(self, other):
        if not self.__check_type_other(other):
            raise ArithmeticError('значение должно быть int или float')

        self.lst_math = [x - other for x in self.lst_math]
        return self

    def __mul__(self, other):
        if not self.__check_type_other(other):
            raise ArithmeticError('значение должно быть int или float')

        return ListMath([x * other for x in self.lst_math])

    def __rmul__(self, other):
        return ListMath([x * other for x in self.lst_math])

    def __imul__(self, other):
        if not self.__check_type_other(other):
            raise ArithmeticError('значение должно быть int или float')

        self.lst_math = [x * other for x in self.lst_math]
        return self

    def __truediv__(self, other):
        if not self.__check_type_other(other):
            raise ArithmeticError('значение должно быть int или float')

        return ListMath([x / other for x in self.lst_math])

    def __rtruediv__(self, other):
        return ListMath([x / other for x in self.lst_math])

    def __itruediv__(self, other):
        if not self.__check_type_other(other):
            raise ArithmeticError('значение должно быть int или float')

        self.lst_math = [x / other for x in self.lst_math]
        return self
