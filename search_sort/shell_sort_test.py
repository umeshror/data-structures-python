from unittest import TestCase

from search_sort.shell_sort import shell_sort


class SelectionSortTest(TestCase):
    def test(self):
        self.assertEqual(shell_sort([-12, 431, 12, 5]), [-12, 5, 12, 431])
        self.assertEqual(shell_sort([-1, -2, -12, -4]), [-12, -4, -2, -1])
        self.assertEqual(shell_sort([11, -2, 0, -4]), [-4, -2, 0, 11])


