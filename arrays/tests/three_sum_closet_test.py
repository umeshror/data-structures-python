import unittest

from arrays.three_sum_closet import three_sum_closet


class TestThreeSum(unittest.TestCase):
    def test(self):
        self.assertEqual(three_sum_closet([-1, 2, 1, -4], 1), 2)
        self.assertEqual(three_sum_closet([2, 2, 1, -4, 3], 5), 5)
        self.assertEqual(three_sum_closet([-1, 2, 1, -4, 3, 5, 12, 6, 36, 4, 1], 2),2)
        self.assertEqual(three_sum_closet([2, 2, 1], 5), 5)
        self.assertEqual(three_sum_closet([2, 2, 1], 0), 5)
        self.assertEqual(three_sum_closet([2, 2, 1, 6], 0), 5)
        self.assertEqual(three_sum_closet([2, 2, 1, 6], 3), 5)
