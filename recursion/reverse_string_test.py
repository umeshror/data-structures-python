from unittest import TestCase

from recursion.reverse_string import reverse_string


class TestReverse(TestCase):
    def test_rev(self):
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string('hello world'), 'dlrow olleh')
        self.assertEqual(reverse_string('123456789'), '987654321')
