class Translator:
    d = {}

    def add(self, eng, rus):
        if eng not in self.d.keys():
            self.d[eng] = [rus]
        else:
            self.d[eng].append(rus)

    def remove(self, eng):
        if eng in self.d.keys():
            del self.d[eng]

    def translate(self, eng):
        if eng in self.d.keys():
            return self.d[eng]


tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')
tr.remove('car')
print(*tr.translate('go'))
