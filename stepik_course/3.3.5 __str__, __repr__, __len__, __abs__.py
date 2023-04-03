class ObjList:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len_lst = 0

    def __len__(self):
        return self.len_lst

    def __call__(self, indx, *args, **kwargs):
        return self.linked_lst(indx)

    def add_obj(self, obj):
        if self.head == None:
            self.head = obj
            self.tail = obj
            self.len_lst += 1

        elif self.head != None and self.tail != None:
            tmp = self.tail
            tmp.next = obj
            self.tail = obj
            self.tail.prev = tmp
            self.len_lst += 1

    def remove_obj(self, indx):
        if indx == 0 and self.len_lst == 1:
            self.head = None
            self.tail = None
            self.len_lst = 0

        elif indx == 0 and self.len_lst > 1:
            node = self.head.next
            node.prev = None
            self.head = node
            self.len_lst -= 1

        elif indx == self.len_lst - 1 and self.len_lst > 1:
            node = self.tail.prev
            node.next = None
            self.tail = node
            self.len_lst -= 1

        elif indx != 0 and indx != self.len_lst - 1:
            node = self.head
            for i in range(indx):
                node = node.next
            left = node.prev
            right = node.next
            left.next = right
            right.prev = left
            self.len_lst -= 1

    def linked_lst(self, indx):
        if indx == 0:
            return self.head.data

        elif indx == self.len_lst - 1:
            return self.tail.data

        elif indx != 0 and indx != self.len_lst - 1:
            node = self.head
            for i in range(indx):
                node = node.next
            return node.data
