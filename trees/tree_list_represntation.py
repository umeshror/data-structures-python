class BinaryTree(object):
    def __init__(self, root):
        """
        root  Left  Right
        [root, [], []]
        """
        self.root = [root, [], []]

    def insert_left(self, new_branch):
        t = self.root.pop(1)
        if len(t) > 1:
            self.root.insert(1, [new_branch, t, []])
        else:
            self.root.insert(1, [new_branch, [], []])
        return self.root

    def insert_right(self, new_branch):
        t = self.root.pop(2)
        if len(t) > 1:
            self.root.insert(2, [new_branch, [], t])
        else:
            self.root.insert(2, [new_branch, [], []])
        return self.root

    def get_root_val(self):
        return self.root[0]

    def set_root_val(self, newVal):
        self.root[0] = newVal

    def get_left_child(self):
        return self.root[1]

    def get_right_child(self):
        return self.root[2]


r = BinaryTree(3)

print r.insert_left(2)
print r.insert_left(1)
print r.insert_right(4)
print r.insert_right(5)