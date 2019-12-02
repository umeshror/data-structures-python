import unittest

from arrays.four_sum import four_sum


class TestFourSum(unittest.TestCase):
    def test(self):
        self.assertCountEqual(four_sum([0, -1, 1], 0), [])
        self.assertCountEqual(four_sum([1, 0, -1, 0, -2, 2], 2), [(-1, 0, 1, 2)])
        self.assertCountEqual(four_sum([1, 0, -1, 0, -2, 2], 0), [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)])
        self.assertCountEqual(four_sum([-3, -2, -1, 0, 0, 1, 2, 3], 0),
                              [(-2, -1, 0, 3), (-3, 0, 1, 2), (-2, -1, 1, 2), (-3, 0, 0, 3), (-3, -1, 1, 3),
                               (-2, 0, 0, 2), (-3, -2, 2, 3), (-1, 0, 0, 1)])
