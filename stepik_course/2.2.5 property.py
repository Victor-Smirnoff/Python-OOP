class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        tmp = self.__width
        if isinstance(value, int) and 0 <= value <= 10000:
            self.__width = value
        if tmp != self.__width:
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        tmp = self.__height
        if isinstance(value, int) and 0 <= value <= 10000:
            self.__height = value
        if tmp != self.__height:
            self.show()
