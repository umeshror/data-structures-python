"""
Given the root of a binary search tree and 2 numbers min and max, trim the tree
 such that all the numbers in the new tree are between min and max (inclusive).
 The resulting tree should still be a valid binary search tree
"""


class Node(object):
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


def trim_bst(tree, min_val, max_val):
    if not tree:
        return

    tree.left = trim_bst(tree.left, min_val, max_val)
    tree.right = trim_bst(tree.right, min_val, max_val)

    if min_val <= tree.val <= max_val:
        return tree

    if tree.val < min_val:
        # being BST all elements will lower than this
        return tree.right

    if tree.val > max_val:
        return tree.left


root = Node(1)

root.left = Node(2)
root.right = Node(3)
trim_bst(root, 1, 1)
