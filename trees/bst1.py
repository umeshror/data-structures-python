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
        # if it has any children then assign those children to its parent
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

    def find_successor(self):
        """
        Finds correct successor if the Node is removed
        :return: Node
        """
        succ = None
        if self.right_child:
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        """
        if we have root then go left/right else assign it as root
        :param key: index
        :param val: data/payload
        """
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = Node(key, val)
        self.size = self.size + 1

    def _put(self, key, val, current_node):
        """
        :param key: index
        :param val: data/payload
        :param current_node: at what node it need to add.
        """
        # given key/index is is less than root/node' key so go left
        if key < current_node.key:
            # we still have left child so go further left if it has left child
            if current_node.left_child:
                self._put(key, val, current_node.left_child)
            # we dont have left child so assign it to left
            else:
                current_node.left_child = Node(key, val, parent=current_node)
        # given key/index is is less than root/node' key so go right
        else:
            # we still have right child so go further right
            if current_node.right_child:
                self._put(key, val, current_node.right_child)
            # we dont have right child so assign it to left
            else:
                current_node.right_child = Node(key, val, parent=current_node)

    def __setitem__(self, k, v):
        """
        magic method to use it as tree[key] = value
        call put internally
        """
        self.put(k, v)

    def get(self, key):
        """
        finds given key in BST and returns its data
        :param key: index
        :return: data
        """
        if self.root:
            node = self._get(key, self.root)
            if node:
                return node.data

    def _get(self, key, current_node):
        """
        finds given key on current_node and returns current_node
        :param key: index
        :param current_node: root node/current node
        :return: current_node
        """
        if not current_node:
            return None
        # given key is mathces current_node's key so return current_node
        elif current_node.key == key:
            return current_node
        # given key is lower than current_node's key so go left
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
            # given key is greater than current_node's key so go right
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        """
        magic method to use it as return tree[key]
        call _get internally
        """
        return self.get(key)

    def __contains__(self, key):
        """
        Finds if given key exists in Tree
        :param key: ind
        :return: True/False
        """
        if self._get(key, self.root):
            return True
        return False

    def delete(self, key):
        """
        Deletes Node of given key
        :param key: ind
        """
        if self.size > 1:
            # find node for given key
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        """
        magic method to delete Node fro given key
        call delete internally
        """
        self.delete(key)

    def find_min(self):
        """
        finds min of the BST
        :return: Node
        """
        current = self
        while current.left_child:
            current = current.left_child
        return current

    def remove(self, current_node):
        """
        Removes provided Node from BST and balances it
        :param current_node: Node
        """

        if current_node.isLeaf():  # leaf
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():  # interior

            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.data = succ.data

        else:  # this node has one child
            if current_node.left_child:
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:

                    current_node.replace_node_data(current_node.left_child.key,
                                                   current_node.left_child.data,
                                                   current_node.left_child.left_child,
                                                   current_node.left_child.right_child)
            else:

                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                                   current_node.right_child.data,
                                                   current_node.right_child.left_child,
                                                   current_node.right_child.right_child)


mytree = BinarySearchTree()
mytree[3] = "red"
mytree[4] = "blue"
mytree[6] = "yellow"
mytree[2] = "at"

print(mytree[6])
print(mytree[2])
