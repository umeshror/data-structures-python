from unittest import TestCase

from maths.integer_to_roman import integer_to_roman, integer_to_roman_sol2


class IntegerToRomanTest(TestCase):
    def test_sol1(self):
        self.assertEqual(integer_to_roman(3), "III")
        self.assertEqual(integer_to_roman(4), "IV")
        self.assertEqual(integer_to_roman(8), "VIII")
        self.assertEqual(integer_to_roman(58), "LVIII")
        self.assertEqual(integer_to_roman(588), "DLXXXVIII")
        self.assertEqual(integer_to_roman(3999), "MMMCMXCIX")

    def test_sol2(self):
        self.assertEqual(integer_to_roman_sol2(3), "III")
        self.assertEqual(integer_to_roman_sol2(4), "IV")
        self.assertEqual(integer_to_roman_sol2(8), "VIII")
        self.assertEqual(integer_to_roman_sol2(58), "LVIII")
        self.assertEqual(integer_to_roman_sol2(588), "DLXXXVIII")
        self.assertEqual(integer_to_roman_sol2(3999), "MMMCMXCIX")
        self.assertEqual(integer_to_roman_sol2(1), "I")
