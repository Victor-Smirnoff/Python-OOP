class Item:
    def __init__(self, name, money):
        if isinstance(name, str):
            self.name = name
        if isinstance(money, (int, float)):
            self.money = money

    def __add__(self, other):
        if isinstance(other, Item):
            return self.money + other.money

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self.money + other


class Budget:
    def __init__(self):
        self.lst_budget = []

    def add_item(self, it):
        if isinstance(it, Item):
            self.lst_budget.append(it)

    def remove_item(self, indx):
        if isinstance(indx, int) and 0 <= indx <= len(self.lst_budget) - 1:
            self.lst_budget.pop(indx)

    def get_items(self):
        return self.lst_budget
