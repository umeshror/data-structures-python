"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
from linked_list.LinkedList import generate_nodes, traverse_list

head_1 = generate_nodes([1, 2, 4])
head_2 = generate_nodes([1, 3, 4])



def merge_two_lists(l1, l2):
    """
    :type l1: Head Node 1 : 1, 2, 4
    :type l2: Head Node 2 : 1, 3, 4
    :rtype: ListNode 1->1->2->3->4->4
    """
    if not l1 or not l2:
        return l1 or l2

    if l1.val < l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2
o = merge_two_lists(head_1, head_2)
print(traverse_list(o))