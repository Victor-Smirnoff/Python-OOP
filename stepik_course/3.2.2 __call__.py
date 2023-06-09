from random import randint

class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.__psw_chars = psw_chars
        self.__min_length = min_length
        self.__max_length = max_length

    def __call__(self, *args, **kwargs):
        return ''.join([self.__psw_chars[randint(0, len(self.__psw_chars) - 1)] for _ in range(randint(self.__min_length, self.__max_length))])


lst_pass = [RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)() for _ in range(3)]
