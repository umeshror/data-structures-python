"""

Write a function to reverse a Linked List in place.
The function will take in the head of the list as input and return the new head of the list.

"""
from linked_list.LinkedList import Node, traverse_list


def reverse(head):
    # Set up current, previous, and next nodes
    current = head
    previous = None
    next = None

    # until we have gone through to the end of the list
    while current:
        # Make sure to copy the current nodes next node to a variable next
        # Before overwriting as the previous node for reversal
        next = current.next

        # Reverse the pointer of the next
        current.next = previous

        # Go one forward in the list
        previous = current
        current = next

    return previous


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.next = b
b.next = c
c.next = d

reverse(a)
print(traverse_list(a))