class BinaryTree(object):
    def __init__(self, node):
        """
                a
            b       c
        """
        self.root = node
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        """
        Check if left_child present
        if present then add element to its left
        """
        if self.left_child:
            self.left_child.insert_left(value)
        else:
            self.left_child = BinaryTree(value)

    def insert_right(self, value):
        if self.right_child:
            self.right_child.insert_left(value)
        else:
            self.right_child = BinaryTree(value)

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child


r = BinaryTree('a')
print(r.get_left_child())
r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().root)
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().root)
