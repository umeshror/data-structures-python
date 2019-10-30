from unittest import TestCase

from arrays.largest_continuous_sum import large_cont_sum_sol


class LargeContTest(TestCase):
    def test(self):
        self.assertEqual(large_cont_sum_sol([1, 2, -1, 3, 4, -1]), 9)
        self.assertEqual(large_cont_sum_sol([1, 2, -1, 3, 4, 10, 10, -10, -1]),29)
        self.assertEqual(large_cont_sum_sol([-1, 1]), 1)
