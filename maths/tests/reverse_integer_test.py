from unittest import TestCase

from maths.reverse_integer import reverse_integer_sol1, reverse_integer_sol2


class KnightDialerTest(TestCase):
    def test_sol1(self):
        self.assertEqual(reverse_integer_sol1(-123), -321)
        self.assertEqual(reverse_integer_sol1(1534236469), 0)
        self.assertEqual(reverse_integer_sol1(-1534236469), 0)
        self.assertEqual(reverse_integer_sol1(123123), 321321)
        self.assertEqual(reverse_integer_sol1(0), 0)

    def test_sol2(self):
        self.assertEqual(reverse_integer_sol2(-123), -321)
        self.assertEqual(reverse_integer_sol2(1534236469), 0)
        self.assertEqual(reverse_integer_sol2(-1534236469), 0)
        self.assertEqual(reverse_integer_sol2(123123), 321321)
        self.assertEqual(reverse_integer_sol2(0), 0)
