class NewList:
    def __init__(self, lst=None):
        self.lst = lst if lst and type(lst) == list else []

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise TypeError('other должен быть списком или объектом NewList')
        tmp_lst = self.lst[:]
        tmp = other
        if isinstance(other, NewList):
            tmp = other.lst[:]

        while tmp:
            for item in tmp:
                if item in tmp_lst:
                    for i in range(len(tmp_lst)):
                        if str(item) == str(tmp_lst[i]):
                            tmp_lst.pop(i)
                            tmp.remove(item)
                            break
                else:
                    tmp.remove(item)

        return NewList(tmp_lst)

    def get_sub_lst_and_obj(self, lst, lst_from_obj):
        if not isinstance(lst, list):
            raise TypeError('other должен быть списком')
        lst = NewList(lst)
        lst = lst.lst[:]
        lst_from_obj = lst_from_obj[:]

        while lst_from_obj:
            for item in lst_from_obj:
                if item in lst:
                    for i in range(len(lst)):
                        if str(item) == str(lst[i]):
                            lst_from_obj.remove(item)
                            lst.pop(i)
                            break
                else:
                    lst_from_obj.remove(item)

        return lst

    def __rsub__(self, other):
        return NewList(self.get_sub_lst_and_obj(other, self.lst))

    def get_list(self):
        return self.lst
