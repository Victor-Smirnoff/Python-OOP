class FloatValue:
    @classmethod
    def verify_float(cls, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_float(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, start_value=0.0):
        self.value = start_value


class TableSheet:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.cells = [[Cell()] * self.M for _ in range(self.N)]


table = TableSheet(5, 3)
tmp = 1.0
for n in range(len(table.cells)):
    for m in range(len(table.cells[n])):
        table.cells[n][m] = Cell(tmp)
        tmp += 1
