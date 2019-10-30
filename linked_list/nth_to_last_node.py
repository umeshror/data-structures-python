"""
Write a function that takes a head node and an integer value n and then returns
the nth to last node in the linked list. For example, given:
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a)
target_node.value
4
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


def nth_to_last_node_sol1(n, head):
    count = 1
    current_node = head

    while current_node.next_node:
        count += 1
        current_node = current_node.next_node
    value_index = count - n

    current_node = head
    while value_index:
        current_node = current_node.next_node
        value_index -= 1

    return current_node.value


def nth_to_last_node_sol2(n, head):
    left_pointer = head
    right_pointer = head

    # Set right pointer at n nodes away from head
    for i in xrange(n - 1):

        # Check for edge case of not having enough nodes!
        if not right_pointer.next_node:
            raise LookupError('Error: n is larger than the linked list.')

        # Otherwise, we can set the block
        right_pointer = right_pointer.next_node

    # Move the block down the linked list
    while right_pointer.next_node:
        left_pointer = left_pointer.next_node
        right_pointer = right_pointer.next_node

    # Now return left pointer, its at the nth to last element!
    return left_pointer.value


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
# 1 2 3 4 5

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e
print nth_to_last_node_sol1(4, a)
print nth_to_last_node_sol2(4, a)
