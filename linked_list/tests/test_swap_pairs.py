import unittest

from linked_list.LinkedList import generate_nodes
from linked_list.add_two_numbers import traverse_list
from linked_list.swap_pairs import swap_pairs


class TestSwapPairs(unittest.TestCase):
    def test_1(self):
        l1 = generate_nodes([1, 2])
        output = swap_pairs(l1)
        self.assertEqual(traverse_list(output), [2, 1])

    def test_2(self):
        l1 = generate_nodes([1, 2, 3])
        output = swap_pairs(l1)
        self.assertEqual(traverse_list(output), [2, 1, 3])

    def test_3(self):
        l1 = generate_nodes([1, 2, 3, 4])
        output = swap_pairs(l1)
        self.assertEqual(traverse_list(output), [2, 1, 4, 3])
