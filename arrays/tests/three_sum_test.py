import unittest

from arrays.three_sum import three_sum_sol2


class TestThreeSum(unittest.TestCase):
    def test(self):
        self.assertCountEqual(three_sum_sol2([-1, 0, 1, 2, -1, -4]), [(-1, -1, 2), (-1, 0, 1)])
        self.assertCountEqual(three_sum_sol2([0, 0, 0]), [(0, 0, 0)])
        self.assertCountEqual(three_sum_sol2([0, 0]), [])
        self.assertCountEqual(three_sum_sol2([0, 0, 0, 0]), [(0, 0, 0)])
        self.assertCountEqual(three_sum_sol2([3, 0, -2, -1, 1, 2]), [(-1, 0, 1), (-2, -1, 3), (-2, 0, 2)])
        self.assertCountEqual(three_sum_sol2([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]),
                              [(-4, -2, 6), (-2, 0, 2), (-2, -2, 4), (-4, 0, 4), (-4, 1, 3), (-4, 2, 2)])
