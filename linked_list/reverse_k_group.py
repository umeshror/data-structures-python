"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of
 the linked list. If the number of nodes is not a multiple of k
  then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
from linked_list.LinkedList import generate_nodes, traverse_list


def reverse_k_group(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    l = 0
    node = head
    while node:
        l += 1
        node = node.next
    if k <= 1 or l < k:
        return head

    cur = head
    node = None
    for _ in range(k):
        nxt = cur.next
        cur.next = node
        node = cur
        cur = nxt
    head.next = reverse_k_group(cur, k)
    return node


head = generate_nodes([1, 2, 3, 4, 5])
out = reverse_k_group(head, 2)
print(traverse_list(out))
