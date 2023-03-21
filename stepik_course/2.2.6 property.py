class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if value == None or isinstance(value, StackObj):
            self.__next = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class Stack:
    def __init__(self):
        self.top = None
        self.tail = None

    def push(self, obj):
        if isinstance(obj, StackObj):
            if self.top == None and self.tail == None:
                self.top = obj
                obj.next = None
            elif self.top != None and self.tail == None:
                self.tail = obj
                self.top.next = obj
            elif self.top != None and self.tail != None:
                self.node = obj
                self.tail.next = self.node
                self.tail = self.node
                self.tail.next = None

    def pop(self):
        if self.top != None:
            if self.tail == None:
                x = self.top
                self.top = None
                return x
            elif self.tail != None:
                self.node = self.top
                x = self.tail
                while self.node.next != self.tail:
                    self.node = self.node.next
                self.node.next = None
                if self.top == self.node:
                    self.tail = None
                    return x
                elif self.top != self.node:
                    self.tail = self.node
                    return x

    def get_data(self):
        tmp_lst = []
        if self.top == None:
            return tmp_lst
        if self.tail == None:
            tmp_lst.append(self.top.data)
            return tmp_lst
        self.tmp_top = self.top
        while self.tmp_top != None:
            tmp_lst.append(self.tmp_top.data)
            self.tmp_top = self.tmp_top.next
        return tmp_lst
