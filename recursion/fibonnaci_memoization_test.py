from unittest import TestCase

from recursion.fibonnaci_memoization import fib_iterative, fib_dynamic, \
    fib_recursion


class TestFib(TestCase):
    def test_fib_iterative(self):
        self.assertEqual(fib_iterative(2), 1)
        self.assertEqual(fib_iterative(8), 21)

    def test_fib_dynamic(self):
        self.assertEqual(fib_dynamic(2), 1)
        self.assertEqual(fib_dynamic(8), 21)
        self.assertEqual(fib_dynamic(12), 144)

    def test_fib_recursion(self):
        self.assertEqual(fib_recursion(2), 1)
        self.assertEqual(fib_recursion(8), 21)
        self.assertEqual(fib_recursion(11), 89)
