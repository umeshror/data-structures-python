from unittest import TestCase

from recursion.word_split import word_split


class BasicRecursionsTest(TestCase):
    def test_word_split(self):
        self.assertEqual(word_split('themanran', ['the', 'ran', 'man']),
                         ['the', 'man', 'ran'])
        self.assertEqual(word_split('themanran', ['clown', 'ran', 'man']), [])
