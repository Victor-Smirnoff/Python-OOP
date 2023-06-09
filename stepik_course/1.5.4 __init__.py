import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


lst_cls = [Line, Rect, Ellipse]
a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
d = random.randint(0, 9)

elements = [random.choice([Line(0, 0, 0, 0), Rect(a, b, c, d), Ellipse(a, b, c, d)]) for _ in range(217)]
