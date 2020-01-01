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
from queue import PriorityQueue

from linked_list.LinkedList import generate_nodes, traverse_list, Node


def merge_k_lists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    head = point = Node(0)
    q = PriorityQueue()
    for l in lists:
        q.put((l.val, id(l), l))

    while not q.empty():
        # get the lowest from queue
        val, _id, node = q.get()
        point.next = Node(val)
        point = point.next
        node = node.next
        if node:
            q.put((node.val, id(node), node))
    return head.next


head_1 = generate_nodes([1, 4, 5])
head_2 = generate_nodes([1, 3, 4])
head_3 = generate_nodes([2, 6])
head_4 = generate_nodes([1, 1])

o = merge_k_lists([head_1, head_2, head_3, head_4])
print(traverse_list(o))
