from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        return len(number.split('-')) == 4 and all([x for x in number.split('-') if x.isdigit() and len(x) == 4])

    @staticmethod
    def check_name(name):
        return set(name) <= set(CardCheck.CHARS_FOR_NAME) and len(name.split(' ')) == 2
