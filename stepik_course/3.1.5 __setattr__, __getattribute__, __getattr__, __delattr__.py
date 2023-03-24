class LessonItem:
    ATTR = {'title': [str], 'practices': [int], 'duration': [int]}

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key in self.ATTR and type(value) not in self.ATTR[key]:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in self.ATTR and self.ATTR[key] == type(value):
            if type(value) == int and value <= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)

    def __getattr__(self, item):
        if item not in ('title', 'practices', 'duration'):
            return False

    def __delattr__(self, item):
        if item not in self.ATTR:
            return super().__delattr__(item)


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        if indx <= len(self.lessons) - 1:
            self.lessons.pop(indx)


class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        if indx <= len(self.modules) - 1:
            self.modules.pop(indx)
