stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

pattern = "–?!,.;"
res_stich = ["".join([x for x in s if x not in pattern]).split() for s in stich]


class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __len__(self):
        return len(self.lst_words)

    def __gt__(self, other):
        if isinstance(other, StringText):
            return len(self) > len(other)

    def __ge__(self, other):
        if isinstance(other, StringText):
            return len(self) >= len(other)

    # def __repr__(self):
    #     return f"{' '.join(self.lst_words)}"


lst_text = [StringText(string) for string in res_stich]

lst_text_sorted = sorted(lst_text, key=lambda x: len(x), reverse=True)

lst_text_sorted = [' '.join(x.lst_words) for x in lst_text_sorted]
