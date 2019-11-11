from unittest import TestCase

from search_sort.merge_sort import merge_sort


class MergeSortTest(TestCase):
    def test(self):
        self.assertEqual(merge_sort([-12, 431, 12, 5]), [-12, 5, 12, 431])
        self.assertEqual(merge_sort([-1, -2, -12, -4]), [-12, -4, -2, -1])
        self.assertEqual(merge_sort([11, -2, 0, -4]), [-4, -2, 0, 11])

