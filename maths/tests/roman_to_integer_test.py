from unittest import TestCase

from maths.roman_to_integer import roman_to_int


class IntegerToRomanTest(TestCase):
    def test_sol(self):
        self.assertEqual(roman_to_int("III"), 2)
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("VIII"), 8)
        self.assertEqual(roman_to_int("IX"), 9)
        self.assertEqual(roman_to_int("LVIII"), 58)
        self.assertEqual(roman_to_int("DLXXXVIII"), 588)
        self.assertEqual(roman_to_int("MMMCMXCIX"), 3999)
