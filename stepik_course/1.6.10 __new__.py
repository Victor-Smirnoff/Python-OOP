class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


class Factory:
    def build_sequence(self):
        self.lst = []
        return self.lst

    def build_number(self, string):
        if type(string) == str:
            return float(string)
