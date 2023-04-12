class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    def __len__(self):
        return len(self.book_list)

    def __add__(self, other):
        if not isinstance(other, Book):
            raise ArithmeticError("Добавлять можно только объекты класса Book")
        self.book_list.append(other)

        return self

    def __iadd__(self, other):
        if not isinstance(other, Book):
            raise ArithmeticError("Добавлять можно только объекты класса Book")
        self.book_list.append(other)

        return self

    def __sub__(self, other):
        if not isinstance(other, (int, Book)):
            raise ArithmeticError("Удалять можно только объекты класса Book или по индексу")
        if type(other) == Book:
            if other not in self.book_list:
                raise NameError("Такой книги нет в библиотеке")
            self.book_list.remove(other)
        if type(other) == int:
            if 0 <= other <= len(self.book_list) - 1:
                self.book_list.pop(other)

        return self

    def __isub__(self, other):
        if not isinstance(other, (int, Book)):
            raise ArithmeticError("Удалять можно только объекты класса Book или по индексу")
        if type(other) == Book:
            if other not in self.book_list:
                raise NameError("Такой книги нет в библиотеке")
            self.book_list.remove(other)
        if type(other) == int:
            if 0 <= other <= len(self.book_list) - 1:
                self.book_list.pop(other)

        return self
