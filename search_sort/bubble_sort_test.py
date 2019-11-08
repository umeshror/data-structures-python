from unittest import TestCase

from search_sort.bubble_sort import bubble_sort


class BubbleSortTest(TestCase):
    def test(self):
        self.assertEqual(bubble_sort([-12, 431, 12, 5]), [-12, 5, 12, 431])
        self.assertEqual(bubble_sort([-1, -2, -12, -4]), [-12, -4, -2, -1])
        self.assertEqual(bubble_sort([-1.1, 2, 0, 5, -33]),[-33, -1.1, 0, 2, 5])


