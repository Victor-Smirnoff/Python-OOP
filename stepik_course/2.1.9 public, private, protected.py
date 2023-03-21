class ObjList:
    def __init__(self, data: str, next=None, prev=None):
        self.__next = next
        self.__prev = prev
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.lst = []
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        if not self.lst:
            self.lst.append(obj)
            obj.set_prev(None)
            obj.set_next(None)
            self.head = self.lst[0]
        elif self.lst:
            self.lst.append(obj)
            obj.set_prev(self.lst[-2])
            obj.set_next(None)
            self.lst[-2].set_next(obj)
            self.tail = self.lst[-1]

    def remove_obj(self):
        if self.lst:
            self.lst.pop()
            if len(self.lst) >= 1:
                self.head = self.lst[0]
                self.lst[-1].set_next(None)
            else:
                self.head = None
            if len(self.lst) >= 2:
                self.head = self.lst[0]
                self.tail = self.lst[-1]

    def get_data(self):
        return [obj.get_data() for obj in self.lst]
