class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        if indx <= len(self.goods) - 1:
            self.goods.remove(self.goods[indx])

    def get_list(self):
        return [f'{self.goods[i].name}: {self.goods[i].price}' for i in range(len(self.goods))]

cart = Cart()
cart.add(TV('Atlant XS500', 7000))
cart.add(TV('Atlant XS550', 8000))
cart.add(Table('IKEA', 2000))
cart.add(Notebook('MSI 5', 60000))
cart.add(Notebook('MSI 6', 80000))
cart.add(Cup('hotcup', 500))
