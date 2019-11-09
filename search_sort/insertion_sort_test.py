from unittest import TestCase

from search_sort.insertion_sort import insertion_sort_sol1


class SelectionSortTest(TestCase):
    def test(self):
        self.assertEqual(insertion_sort_sol1([-12, 431, 12, 5]), [-12, 5, 12, 431])
        self.assertEqual(insertion_sort_sol1([-1, -2, -12, -4]), [-12, -4, -2, -1])
        self.assertEqual(insertion_sort_sol1([-12, 431, 12, 5]), [-12, 5, 12,
                                                                431])
        self.assertEqual(insertion_sort_sol1([-1, -2, -12, -4]), [-12, -4, -2, -1])


