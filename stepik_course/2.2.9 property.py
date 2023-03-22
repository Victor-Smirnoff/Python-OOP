class LineTo:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value


class PathLines:
    def __init__(self, *args):
        self.LST_LINES = []  # append of objects of class LineTo
        for arg in args:
            self.LST_LINES.append(arg)

    def get_path(self):
        return self.LST_LINES

    def get_length(self):
        res_length = 0
        if len(self.LST_LINES) == 0:
            return 0
        for i in range(len(self.LST_LINES)):
            if len(self.LST_LINES) == 1:
                res_length += (self.LST_LINES[0].x ** 2 + self.LST_LINES[0].y ** 2) ** 0.5
                return res_length
            if i == 0:
                res_length += (self.LST_LINES[0].x ** 2 + self.LST_LINES[0].y ** 2) ** 0.5
            else:
                res_length += ((self.LST_LINES[i].x - self.LST_LINES[i - 1].x) ** 2 + (self.LST_LINES[i].y - self.LST_LINES[i - 1].y) ** 2) ** 0.5
        return res_length

    def add_line(self, line):
        self.LST_LINES.append(line)
