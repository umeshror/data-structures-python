from unittest import TestCase

from strings.phone_letter_comb import find_combinations


class PhoneLetterCombTest(TestCase):
    def test(self):
        self.assertEqual(find_combinations("23"), ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
        self.assertEqual(find_combinations("0"), [])
        self.assertEqual(find_combinations("232d"), [])
        self.assertEqual(find_combinations("2ee2.2"), [])
        self.assertEqual(find_combinations("1"), [])
        self.assertEqual(find_combinations("2"), ['a', 'b', 'c'])
