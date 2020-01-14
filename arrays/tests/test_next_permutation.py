import unittest

from arrays.next_permutation import next_permutation_sol2


class TestThreeSum(unittest.TestCase):
    def test(self):
        self.assertEqual(next_permutation_sol2([1, 2, 3]), [1, 3, 2])
        self.assertEqual(next_permutation_sol2([1, 1, 3, 3]), [1, 3, 1, 3])
        self.assertEqual(next_permutation_sol2([2, 1, 3]), [2, 3, 1])
        self.assertEqual(next_permutation_sol2([3, 2, 1]), [1, 2, 3])
