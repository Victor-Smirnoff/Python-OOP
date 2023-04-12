class FileAcceptor:
    def __init__(self, *args):
        self.lst = list(args)

    def __eq__(self, other):
        if isinstance(other, str):
            return other in self.lst

    def __add__(self, other):
        if isinstance(other, FileAcceptor):
            tmp_lst = self.lst[:]
            for acc in other.lst:
                if acc not in tmp_lst:
                    tmp_lst.append(acc)
        return FileAcceptor(*tmp_lst)

    def __call__(self, filename):
        return filename.split('.')[-1] in self.lst
