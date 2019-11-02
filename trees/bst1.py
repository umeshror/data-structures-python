class Node(object):
    """
    Every Node has a key and data.
    Node has a parent Node and 2 childrens left annd right
    """
    def __init__(self, key, val, parent=None):
        self.key = key
        self.data = val
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def is_left_child(self):
        """
        Returns if self is left child of its parent
        :return True/False
        """
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        """
        Returns if self is right child of its parent
        :return True/False
        """
        return self.parent and self.parent.right_child == self

    def is_root(self):
        """
        Returns if node is root node
        :return True/False
        """
        return not self.parent

    def is_leaf(self):
        """
        Returns if node is leaf node(if no child exist)
        :return True/False
        """
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        """
        Returns if node has either right_child or right_child
        :return True/False
        """
        return self.right_child or self.left_child

    def has_both_children(self):
        """
        Returns if node has both right_child or right_child
        :return True/False
        """
        return self.right_child and self.left_child

    def replace_node_data(self, key, val, left_child, right_child):
        """
        Replaces Node values with new ones
        :param key:  
        :param val: 
        :param left_child: 
        :param right_child: 
        :return: 
        """
        self.key = key
        self.data = val
        self.left_child = left_child
        self.right_child = right_child
        # replaces parent of bith child's to new self
        if self.left_child:
            self.left_child.parent = self
        if self.right_child:
            self.right_child.parent = self

    def splice_out(self):
        """
        Splices out the node from tree and assign its childs to parent
        :return:
        """
        # if node is leaf node then remove its entry from its parent
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        # if it has any children then assign those children to parent
        elif self.has_any_children():
            if self.left_child:
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:

                    self.parent.right_child = self.left_child
                    self.left_child.parent = self.parent
        else:
            if self.is_left_child():

                self.parent.left_child = self.right_child
            else:
                self.parent.right_child = self.right_child
                self.right_child.parent = self.parent


