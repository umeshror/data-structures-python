"""

Write a function to reverse a Linked List in place.
The function will take in the head of the list as input and return the new head of the list.

"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


def reverse(head):
    # Set up current, previous, and next nodes
    current = head
    previous = None
    next_node = None

    # until we have gone through to the end of the list
    while current:
        # Make sure to copy the current nodes next node to a variable next_node
        # Before overwriting as the previous node for reversal
        next_node = current.next_node

        # Reverse the pointer of the next_node
        current.next_node = previous

        # Go one forward in the list
        previous = current
        current = next_node

    return previous


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.next_node = b
b.next_node = c
c.next_node = d

reverse(a)
print d.next_node.value
print c.next_node.value
print b.next_node.value
