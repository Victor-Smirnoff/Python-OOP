class Model:
    def __init__(self):
        self.__bd = {}

    def query(self, **kwargs):
        self.__bd = kwargs

    def __repr__(self):
        return "Model" if len(self.__bd) == 0 else f"Model: " + ', '.join([str(key) + ' = ' + str(value) for key, value in self.__bd.items()])


model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)
