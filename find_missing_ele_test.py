import unittest

from find_missing_ele import finder_sol1


class TestFinder(unittest.TestCase):
    def test_finder_sol1(self):
        self.assertEqual(finder_sol1([5, 5, 7, 7], [5, 7, 7]), 5)
        self.assertEqual(finder_sol1([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]),
                         5)
        self.assertEqual(finder_sol1([9, 8, 7, 6, 5, 4, 3, 2, 1],
                                     [9, 8, 7, 5, 4, 3, 2, 1]), 6)

    def test_finder_sol2(self):
        arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 88]
        arr2 = [3, 7, 2, 1, 4, 6]
        self.assertEqual(finder_sol1(arr1, arr2), [5, 8, 88])
        self.assertEqual(finder_sol1([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]),
                         5)
        self.assertEqual(finder_sol1([9, 8, 7, 6, 5, 4, 3, 2, 1],
                                     [9, 8, 7, 5, 4, 3, 2, 1]), 6)
