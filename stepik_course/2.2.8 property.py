class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value


class DecisionTree:
    root = None
    node = None

    @classmethod
    def predict(cls, root, x):
        root = cls.root
        while root.value == None:
            if x[root.indx]:
                root = root.left
            else:
                root = root.right
        return root.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if cls.root is None:
            cls.root = obj
            obj.left = None
            obj.right = None
            return obj
        if node == cls.root:
            if left == True:
                cls.root.left = obj
            else:
                cls.root.right = obj
            return obj
        if left == True:
            node.left = obj
        else:
            node.right = obj
        return obj
