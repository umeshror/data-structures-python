"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
from linked_list.LinkedList import generate_nodes, traverse_list, Node

head_1 = generate_nodes([1, 4, 5])
head_2 = generate_nodes([1, 3, 4])
head_3 = generate_nodes([2, 6])

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    l1 = lists[0]
    l2 = lists[1]
    if not l1 or not l2:
        return l1 or l2

    if l1.value > l2.value:


