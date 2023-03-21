from random import randint, choice
from string import ascii_letters, digits


class EmailValidator:
    correct_letters = ascii_letters + digits + '_.'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        len_left = randint(1, 100)
        len_rigth = randint(1, 49)
        left, right, dog = '', '', '@'
        for n in range(len_left):
            left += choice(cls.correct_letters)
        for m in range(len_rigth):
            right += choice(cls.correct_letters)
        res = left + dog + right + '.'
        return res

    @classmethod
    def check_email(cls, email: str):
        if not cls.__is_email_str(email):
            return False
        if email.count('@') != 1:
            return False
        if email.count('..') > 0:
            return False
        two_parts = email.split('@')
        if len(two_parts[0]) > 100:
            return False
        if len(two_parts[1]) > 50:
            return False
        if two_parts[1].count('.') < 1:
            return False
        for x in email:
            if x not in cls.correct_letters + '@':
                return False
        return True

    @staticmethod
    def __is_email_str(email):
        return type(email) == str
