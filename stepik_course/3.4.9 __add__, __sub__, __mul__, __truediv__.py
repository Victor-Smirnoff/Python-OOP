class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        if isinstance(other, Box3D):
            w = self.width + other.width
            h = self.height + other.height
            d = self.depth + other.depth
            return Box3D(w, h, d)

    def __sub__(self, other):
        if isinstance(other, Box3D):
            w = self.width - other.width
            h = self.height - other.height
            d = self.depth - other.depth
            return Box3D(w, h, d)

    def __mul__(self, other):
        if isinstance(other, int):
            w = self.width * other
            h = self.height * other
            d = self.depth * other
            return Box3D(w, h, d)

    def __rmul__(self, other):
        return self * other

    def __floordiv__(self, other):
        if isinstance(other, int):
            w = int(self.width // other)
            h = int(self.height // other)
            d = int(self.depth // other)
            return Box3D(w, h, d)

    def __mod__(self, other):
        if isinstance(other, int):
            w = int(self.width % other)
            h = int(self.height % other)
            d = int(self.depth % other)
            return Box3D(w, h, d)
