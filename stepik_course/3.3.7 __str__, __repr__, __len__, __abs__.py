class RadiusVector:
    def __init__(self, n, *args):
        if len(args) == 0 and type(n) == int and n > 0:
            self.n = n
            self.coords = [0] * self.n
        else:
            self.coords = [n] + list(args)

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        res_abs = 0
        for x in self.coords:
            res_abs += x ** 2
        return res_abs ** 0.5

    def get_coords(self):
        return tuple(self.coords)

    def set_coords(self, *args):
        if len(args) == len(self.coords):
            self.coords = list(args)
        elif len(args) < len(self.coords):
            self.coords = list(args) + self.coords[len(args):]
        elif len(args) > len(self.coords):
            self.coords = args[:len(self.coords)]
