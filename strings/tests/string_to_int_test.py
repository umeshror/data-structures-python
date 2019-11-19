from unittest import TestCase

from strings.string_to_int import strng_to_int


class StrngToIntTest(TestCase):
    def test(self):
        self.assertEqual(strng_to_int("42"), 42)
        self.assertEqual(strng_to_int("    -42 afd"), -42)
        self.assertEqual(strng_to_int("4193 with words"), 4193)
        self.assertEqual(strng_to_int("words and 987"), 0)
        self.assertEqual(strng_to_int("-91283472332"), -2147483648)
        self.assertEqual(strng_to_int("- 1 as "), 0)
        self.assertEqual(strng_to_int(""), 0)
        self.assertEqual(strng_to_int(" 112 112"), 112)
