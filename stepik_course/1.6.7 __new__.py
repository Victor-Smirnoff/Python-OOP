class SingletonFive:
    __instance = None
    count = 0

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls.count < 5:
            cls.__instance = super().__new__(cls)
            cls.count += 1
            return cls.__instance
        else:
            return cls.__instance


objs = [SingletonFive(str(n)) for n in range(10)]
