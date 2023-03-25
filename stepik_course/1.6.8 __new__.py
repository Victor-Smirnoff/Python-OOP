TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            d1 = DialogWindows()
            setattr(d1, 'name', *args)
            return d1
        d0 = DialogLinux()
        setattr(d0, 'name', *args)
        return d0
