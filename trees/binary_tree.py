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

def pre_order(tree):
    """
    Traversal: root > then left > then right:
                1
         2            3
    4        5
    > 1 2 4 5 3
    """
    if tree:
        print(tree.root)
        post_order(tree.get_left_child())
        post_order(tree.get_right_child())


def in_order(tree):
    """
    Traversal: left > then root > then right:
                1
         2            3
    4        5
    > 4 2 5 1 3
    """
    if tree:
        post_order(tree.get_left_child())
        print(tree.root)
        post_order(tree.get_right_child())

def post_order(tree):
    """
    Traversal: left > then right > then root:
                1
         2            3
    4        5
    > 4 5 2 3 1
    """

    if tree:
        post_order(tree.get_left_child())
        post_order(tree.get_right_child())
        print(tree.root)



r = BinaryTree('a')
print(r.get_left_child())
r.insert_left('b')
r.insert_left('bb')
print(r.get_left_child())
print(r.get_left_child().root)
r.insert_right('c')
r.insert_right('cc')
print(r.get_right_child())
print(r.get_right_child().root)
pre_order(r)
in_order(r)
post_order(r)
