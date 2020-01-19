from unittest import TestCase

from largest_word import find_largest_sol1, find_largest_sol2


class TestFindLargest(TestCase):
    def test_sol1(self):
        self.assertEqual(find_largest_sol1('fun&!! time'), 'time')
        self.assertEqual(find_largest_sol1('fun&!! time&'), None)
        self.assertEqual(find_largest_sol1('I love dogs'), 'love')
        self.assertEqual(find_largest_sol1('I love dogs'), 'love')
        self.assertEqual(find_largest_sol1('I love1 dogs'), 'dogs')
        self.assertEqual(find_largest_sol1(''), None)

    def test_sol2(self):

        self.assertEqual(find_largest_sol2('fun&!! time'), 'time')
        self.assertEqual(find_largest_sol2('fun&!! time&'), None)
        self.assertEqual(find_largest_sol2('I love dogs'), 'love')
        self.assertEqual(find_largest_sol2('I love dogs'), 'love')
        self.assertEqual(find_largest_sol2('I love1 dogs'), 'dogs')
        self.assertEqual(find_largest_sol2(''), None)