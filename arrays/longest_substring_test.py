from unittest import TestCase

from arrays.longest_substring import length_of_longest_substring



class LongestSubStrTest(TestCase):
    def test(self):
        self.assertEqual(length_of_longest_substring(" "), 1)
        self.assertEqual(length_of_longest_substring("dvdf"), 3)
        self.assertEqual(length_of_longest_substring("ynyo"), 3)
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)
