class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        flag = True
        for i in range(len(self.apps)):
            if type(self.apps[i]) == type(app):
                flag = False
                break
        if flag == True:
            self.apps.append(app)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)


class AppVK:
    def __init__(self, name='ВКонтакте'):
        self.name = name


class AppYouTube:
    def __init__(self, memory_max, name='YouTube'):
        self.memory_max = memory_max
        self.name = name


class AppPhone:
    def __init__(self, phone_list, name='Phone'):
        self.phone_list = phone_list
        self.name = name
