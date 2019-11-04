import unittest

from linked_list.add_two_numbers import add_two_numbers, Node, traverse_list


class TestAddTwoNumbers(unittest.TestCase):
    def test_1(self):
        l1 = Node(2)
        node2 = Node(4)
        node3 = Node(3)

        l1.next = node2
        node2.next = node3

        l2 = Node(5)
        node2 = Node(6)
        node3 = Node(4)

        l2.next = node2
        node2.next = node3

        final_ll = add_two_numbers(l1, l2)

        self.assertEqual(traverse_list(final_ll), [7, 0, 8])

    def test_2(self):
        l1 = Node(2)
        node2 = Node(4)
        node3 = Node(3)

        l1.next = node2
        node2.next = node3

        l2 = Node(5)
        node2 = Node(6)

        l2.next = node2

        final_ll = add_two_numbers(l1, l2)

        self.assertEqual(traverse_list(final_ll), [7, 0, 4])

    def test_3(self):
        l1 = Node(5)

        l2 = Node(5)

        final_ll = add_two_numbers(l1, l2)

        self.assertEqual(traverse_list(final_ll), [0, 1])
