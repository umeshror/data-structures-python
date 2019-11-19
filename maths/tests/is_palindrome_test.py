from unittest import TestCase

from maths.reverse_integer import reverse_integer_sol1, reverse_integer_sol2


class IsPalindromeTest(TestCase):
    def test_sol1(self):
        self.assertFalse(reverse_integer_sol1(-123))
        self.assertFalse(reverse_integer_sol1(123))
        self.assertFalse(reverse_integer_sol1(123321))
        self.assertTrue(reverse_integer_sol1(0))
        self.assertTrue(reverse_integer_sol1(12121))

    def test_sol2(self):
        self.assertFalse(reverse_integer_sol2(-123))
        self.assertFalse(reverse_integer_sol2(123))
        self.assertFalse(reverse_integer_sol2(123321))
        self.assertTrue(reverse_integer_sol2(0))
        self.assertTrue(reverse_integer_sol2(12121))
