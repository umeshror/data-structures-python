class BinaryTree(object):
    def __init__(self, root):
        """
        root  Left  Right
        [root, [], []]
        """
        self.root = [root, [], []]

    def insertLeft(self, newBranch):
        t = self.root.pop(1)
        if len(t) > 1:
            self.root.insert(1, [newBranch, t, []])
        else:
            self.root.insert(1, [newBranch, [], []])
        return self.root

    def insertRight(self, newBranch):
        t = self.root.pop(2)
        if len(t) > 1:
            self.root.insert(2, [newBranch, [], t])
        else:
            self.root.insert(2, [newBranch, [], []])
        return self.root

    def getRootVal(self):
        return self.root[0]

    def setRootVal(self, newVal):
        self.root[0] = newVal

    def getLeftChild(self):
        return self.root[1]

    def getRightChild(self):
        return self.root[2]


r = BinaryTree(3)

print r.insertLeft(2)
print r.insertLeft(1)
print r.insertRight(4)
print r.insertRight(5)