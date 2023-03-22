class PhoneNumber:
    def __init__(self, number: int, fio: str):
        if isinstance(number, int) and len(str(number)) == 11:
            self.__number = number
        if isinstance(fio, str):
            self.__fio = fio

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = number

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, value):
        self.__fio = fio


class PhoneBook:
    def __init__(self):
        self.lst = []

    def add_phone(self, phone):
        self.lst.append(phone)

    def remove_phone(self, indx):
        self.lst.pop(indx)

    def get_phone_list(self):
        return self.lst
