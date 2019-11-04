"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def addTwoNumbers(l1, l2, carry=0):
    """
    :type l1: Node
    :type l2: Node
    :rtype: Node
    """
    val = l1.val + l2.val + carry
    carry = val // 10

    final_ll = Node(val % 10)

    if (l1.next != None or l2.next != None or carry != 0):
        if l1.next == None:
            l1.next = Node(0)
        if l2.next == None:
            l2.next = Node(0)
        final_ll.next = addTwoNumbers(l1.next, l2.next, carry)

    return final_ll

l1 = Node(2)
node2 = Node(4)
node3 = Node(3)

l1.next = node2
node2.next = node3

l2 = Node(5)
node2 = Node(6)
node3 = Node(4)

l2.next = node2
node2.next = node3

addTwoNumbers(l1, l2)

