import unittest

from linked_list.LinkedList import generate_nodes
from linked_list.add_two_numbers import traverse_list
from linked_list.merge_two_sorted_list import merge_two_lists


class TestRemoveNthNode(unittest.TestCase):
    def test_1(self):
        l1 = generate_nodes([1, 2, 4])
        l2 = generate_nodes([1, 3, 4])
        output = merge_two_lists(l1, l2)
        self.assertEqual(traverse_list(output), [1, 1, 2, 3, 4, 4])

    def test_2(self):
        l1 = generate_nodes([])
        l2 = generate_nodes([])
        output = merge_two_lists(l1, l2)
        self.assertEqual(traverse_list(output), [])


    def test_3(self):
        l1 = generate_nodes([5])
        l2 = generate_nodes([1, 2, 4])
        output = merge_two_lists(l1, l2)
        self.assertEqual(traverse_list(output), [1, 2, 4, 5])

