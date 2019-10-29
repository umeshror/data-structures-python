import unittest

from pair_sum import pair_sum_sol1


class TestPair(unittest.TestCase):
    def test_pair(self):
        self.assertEqual(
                pair_sum_sol1(
                        [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1],
                        10), 6)
        self.assertEqual(pair_sum_sol1([1, 2, 3, 1], 3), 2)
        self.assertEqual(pair_sum_sol1([1, 3, 2, 2], 4), 2)
