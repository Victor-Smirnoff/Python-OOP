import time


class Mechanical:
    lst_of_objects = []

    def __init__(self, date):
        self.date = date
        self.lst_of_objects.append(self)

    def __setattr__(self, key, value):
        if key == 'date' and self not in self.lst_of_objects:
            super().__setattr__(key, value)
        if key == 'date' and self in self.lst_of_objects:
            return


class Aragon:
    lst_of_objects = []

    def __init__(self, date):
        self.date = date
        self.lst_of_objects.append(self)

    def __setattr__(self, key, value):
        if key == 'date' and self not in self.lst_of_objects:
            super().__setattr__(key, value)
        if key == 'date' and self in self.lst_of_objects:
            return


class Calcium:
    lst_of_objects = []

    def __init__(self, date):
        self.date = date
        self.lst_of_objects.append(self)

    def __setattr__(self, key, value):
        if key == 'date' and self not in self.lst_of_objects:
            super().__setattr__(key, value)
        if key == 'date' and self in self.lst_of_objects:
            return


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slots = {1: None, 2: None, 3: None}

    def add_filter(self, slot_num, filter):
        if self.slots[slot_num] == None:
            if slot_num == 1 and type(filter) == Mechanical:
                self.slots[slot_num] = filter
            if slot_num == 2 and type(filter) == Aragon:
                self.slots[slot_num] = filter
            if slot_num == 3 and type(filter) == Calcium:
                self.slots[slot_num] = filter

    def remove_filter(self, slot_num):
        if self.slots[slot_num] != None:
            self.slots[slot_num] = None

    def get_filters(self):
        return self.slots[1], self.slots[2], self.slots[3]

    def water_on(self):
        if all(self.get_filters()) and all([0 <= time.time() - self.slots[1].date <= self.MAX_DATE_FILTER,
                                       0 <= time.time() - self.slots[2].date <= self.MAX_DATE_FILTER,
                                       0 <= time.time() - self.slots[3].date <= self.MAX_DATE_FILTER]):
            return True

        return False
