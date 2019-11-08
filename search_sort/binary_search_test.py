from unittest import TestCase

from search_sort.binary_search import binary_search


class BinarySearchTest(TestCase):
    def test(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5, 6], 3))
        self.assertTrue(binary_search([1, 2, 3, 4, 5, 6], 1))
        self.assertFalse(binary_search([1, 2, 3, 4, 5, 6], 44))
