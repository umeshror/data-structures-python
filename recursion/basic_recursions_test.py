from unittest import TestCase

from recursion.basic_recursions import find_fibo, find_sum, sum_func


class BasicRecursionsTest(TestCase):
    def test_find_fibo(self):
        self.assertEqual(find_fibo(5), 120)
        self.assertEqual(find_fibo(0), 1)
        self.assertEqual(find_fibo(3), 6)
        self.assertEqual(find_fibo(1), 1)

    def test_find_sum(self):
        self.assertEqual(find_sum(5), 15)
        self.assertEqual(find_sum(1), 1)
        self.assertEqual(find_sum(0), 0)
        self.assertEqual(find_sum(11), 66)

    def test_sum_func(self):
        self.assertEqual(sum_func(4321), 10)
        self.assertEqual(sum_func(1), 1)
        self.assertEqual(sum_func(0), 0)
        self.assertEqual(sum_func(213412), 13)
