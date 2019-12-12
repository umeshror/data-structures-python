import unittest

from linked_list.LinkedList import generate_nodes
from linked_list.add_two_numbers import traverse_list
from linked_list.remove_nth_node import remove_nth_frm_end


class TestRemoveNthNode(unittest.TestCase):
    def test_1(self):
        arr1 = generate_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        out = remove_nth_frm_end(arr1, 4)
        self.assertEqual(traverse_list(out), [1, 2, 3, 4, 5, 6, 8, 9, 10])

    def test_2(self):
        arr1 = generate_nodes([1, 2, 3])
        out = remove_nth_frm_end(arr1, 1)
        self.assertEqual(traverse_list(out), [1, 2])

    def test_3(self):
        arr1 = generate_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        out = remove_nth_frm_end(arr1, 7)
        self.assertEqual(traverse_list(out), [1, 2, 3, 5, 6, 7, 8, 9, 10])

    def test_4(self):
        arr1 = generate_nodes([1, 2, 3, 4])
        out = remove_nth_frm_end(arr1, 4)
        self.assertEqual(traverse_list(out), [2, 3, 4])
