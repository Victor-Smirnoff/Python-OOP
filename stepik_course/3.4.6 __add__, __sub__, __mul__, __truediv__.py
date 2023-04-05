class StackObj:
    def __init__(self, data):
        self.__data = self.__next = None
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == str:
            self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top == None:
            self.top = obj

        elif self.top != None and self.top.next == None:
            self.top.next = obj

        elif self.top != None and self.top.next != None:
            node = self.top
            while node.next:
                node = node.next
            node.next = obj

    def pop_back(self):
        left = self.top
        right = self.top.next
        while right.next:
            left = right
            right = right.next
        left.next = None

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        if type(other) == list:
            other_stack = Stack()
            for data in other:
                if type(data) == str:
                    other_stack.push_back(StackObj(data))

            node = self.top
            while node.next:
                node = node.next
            node.next = other_stack.top

        return self

    def __imul__(self, other):
        self.__mul__(other)
        return self

    def show(self):
        res = []
        node = self.top
        while node.next:
            res.append(node.data)
            node = node.next
        res.append(node.data)
        print(*res)
