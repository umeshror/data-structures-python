from unittest import TestCase

from search_sort.selection_sort import selection_sort_max, selection_sort_min


class SelectionSortTest(TestCase):
    def test(self):
        self.assertEqual(selection_sort_min([-12, 431, 12, 5]), [-12, 5, 12, 431])
        self.assertEqual(selection_sort_min([-1, -2, -12, -4]), [-12, -4, -2, -1])
        self.assertEqual(selection_sort_max([-12, 431, 12, 5]), [-12, 5, 12,
                                                                431])
        self.assertEqual(selection_sort_max([-1, -2, -12, -4]), [-12, -4, -2, -1])


