"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only
nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
from linked_list.LinkedList import traverse_list, generate_nodes, Node


def swap_pairs(head):
    """
    :type head: Node
    :rtype: Node
    """
    t = prev = Node(0)
    prev.next = head  # 0  1 2 3 4

    while head and head.next:
        prev.next = head.next  # 0  2 3 4
        head.next = head.next.next  # 1  3 4
        prev.next.next = head  # 0 2  1 3 4
        head = head.next  # 3 4
        prev = prev.next.next  # 1 3 4
    return t.next


head = generate_nodes([1, 2, 3, 4])
head = swap_pairs(head)
print(traverse_list(head))
