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
    prev.next = head
    # 0  1 2 3 4
    while head and head.next:
        prev.next = head.next
        head.next = head.next.next
        prev.next.next = head
        head = head.next
        prev = prev.next.next
    return t.next


head = generate_nodes([1, 2, 3, 4])
head = swap_pairs(head)
print(traverse_list(head))
