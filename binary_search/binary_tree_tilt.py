"""
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree
node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input:
         1
       /   \
      2     3
Output: 1
Explanation:
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.
"""
from linked_list.LinkedList import Node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find_tilt(root):
    """
    root: Root Node
    return : tile node
    """

    def rec(r, s):
        if not r:
            return 0
        a, b = rec(r.left, s), rec(r.right, s)
        s += abs(a - b)
        return a + b + r.val
    s = rec(root, 0)
    return s


# Create a list of 4 nodes
root = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

# Set up order a,b,c,d with values 1,2,3,4
root.left = b
root.right = c

print(find_tilt(root))
