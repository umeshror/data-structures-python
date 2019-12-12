"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

"""
from linked_list.LinkedList import Node, generate_nodes, traverse_list


def remove_nth_frm_end(head, n):
    """
    2 pointer algo
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    tmp = Node(-1)
    tmp.next = head

    pointer_1 = tmp
    pointer_2 = tmp

    # Move over n nodes including dummy
    for i in range(n):
        pointer_2 = pointer_2.next  # set pointer_2 to n-1 th

    # Increment ptrs till you reach end of list
    while pointer_2.next:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next
    # Now pointer_1.next points to the nth node from the end
    pointer_1.next = pointer_1.next.next

    return head


hea = remove_nth_frm_end(generate_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 4)
print(traverse_list(hea))