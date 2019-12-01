from unittest import TestCase

from arrays.unique_character import uni_char_sol1


class TestUnique(TestCase):
    def test(self):
        self.assertEqual(uni_char_sol1(''), True)
        self.assertEqual(uni_char_sol1('goo'), False)
        self.assertEqual(uni_char_sol1('abcdefg'), True)
