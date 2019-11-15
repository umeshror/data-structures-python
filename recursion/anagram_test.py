from unittest import TestCase

from recursion.anagram import find_anagram


class BasicRecursionsTest(TestCase):
    def test(self):
        self.assertTrue(find_anagram("bcd", "cbd"))
        self.assertFalse(find_anagram("bcd", "abd"))
        self.assertFalse(find_anagram("ab", "abd"))
        self.assertTrue(find_anagram("abcde", "edbac"))
        self.assertFalse(find_anagram("a", "e"))
        self.assertTrue(find_anagram("a", "a"))
