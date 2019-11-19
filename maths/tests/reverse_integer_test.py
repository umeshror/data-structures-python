from unittest import TestCase

from maths.integer_palindrome import is_palindrome_sol1, is_palindrome_sol2


class ReverseIntegerTest(TestCase):
    def test_sol1(self):
        self.assertEqual(is_palindrome_sol1(-123), -321)
        self.assertEqual(is_palindrome_sol1(1534236469), 0)
        self.assertEqual(is_palindrome_sol1(-1534236469), 0)
        self.assertEqual(is_palindrome_sol1(123123), 321321)
        self.assertEqual(is_palindrome_sol1(0), 0)

    def test_sol2(self):
        self.assertEqual(is_palindrome_sol2(-123), -321)
        self.assertEqual(is_palindrome_sol2(1534236469), 0)
        self.assertEqual(is_palindrome_sol2(-1534236469), 0)
        self.assertEqual(is_palindrome_sol2(123123), 321321)
        self.assertEqual(is_palindrome_sol2(0), 0)
