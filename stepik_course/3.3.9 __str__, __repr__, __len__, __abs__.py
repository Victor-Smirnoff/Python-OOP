class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


class Recipe:
    def __init__(self, *args):
        self.ings = [*args]

    def add_ingredient(self, ing):
        self.ings.append(ing)

    def remove_ingredient(self, ing):
        if ing in self.ings:
            self.ings.remove(ing)

    def get_ingredients(self):
        return tuple(self.ings)

    def __len__(self):
        return len(self.ings)
