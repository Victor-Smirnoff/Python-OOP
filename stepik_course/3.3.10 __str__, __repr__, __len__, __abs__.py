class PolyLine:
    def __init__(self, start_coord, *args):
        self.points = [start_coord] + list(args)

    def add_coord(self, x, y):
        self.points.append((x, y))

    def remove_coord(self, indx):
        if indx <= len(self.points) - 1:
            self.points.pop(indx)

    def get_coords(self):
        return self.points
