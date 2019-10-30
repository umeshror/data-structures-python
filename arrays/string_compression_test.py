from unittest import TestCase

from arrays.string_compression import compress


class TestCompress(TestCase):
    def test_compress(self):
        self.assertEqual(compress(''), '')
        self.assertEqual(compress('AABBCC'), 'A2B2C2')
        self.assertEqual(compress('AAABCCDDDDD'), 'A3B1C2D5')
        self.assertEqual(compress('A'), 'A1')
        self.assertEqual(compress('AAAaaa'), 'A3a3')
