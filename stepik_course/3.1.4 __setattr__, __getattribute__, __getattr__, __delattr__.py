class Product:
    id_of_obj = 0

    @classmethod
    def get_id_of_obj(cls):
        cls.id_of_obj += 1
        return cls.id_of_obj

    def __init__(self, name, weight, price):
        self.id = self.get_id_of_obj()
        self.name = name
        self.weight = weight
        self.price = price

    attrs = {'id': [int], 'name': [str], 'weight': (int, float), 'price': (int, float)}

    def __setattr__(self, key, value):
        if key in self.attrs and type(value) in self.attrs[key]:
            if key == 'weight' and value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")
            if key == 'price' and value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")
            super().__setattr__(key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            super().__delattr__(item)


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)
