class Morph:
    def __init__(self, *args):
        self.forms = [*args]

    def add_word(self, word):
        if word not in self.forms:
            self.forms.append(word)

    def get_words(self):
        return tuple(self.forms)

    def __eq__(self, other):
        return other.lower() in self.forms


dict_words = [Morph("связь", "связи", "связью", "связей", "связям", "связями", "связях"),
              Morph("формула", "формулы", "формуле", "формулу", "формулой", "формул", "формулам", "формулами", "формулах"),
              Morph("вектор", "вектора", "вектору", "вектором", "векторе", "векторы", "векторов", "векторам", "векторами", "векторах"),
              Morph("эффект", "эффекта", "эффекту", "эффектом", "эффекте", "эффекты", "эффектов", "эффектам", "эффектами", "эффектах"),
              Morph("день", "дня", "дню", "днем", "дне", "дни", "дням", "днями", "днях")
              ]

pattern = "–?!,.;"
text = [word.strip(pattern) for word in input().lower().split()]

count = 0

for word in text:
    for obj in dict_words:
        if obj == word:
            count += 1

print(count)
