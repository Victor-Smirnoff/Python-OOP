class Money:
    def __init__(self, money):
        self.__money = 0
        if self.__check_money(money):
            self.__money = money

    @classmethod
    def __check_money(cls, money):
        if type(money) == int and money >= 0:
            return True

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.set_money(self.__money + mn.get_money())
