from unittest import TestCase

from recursion.string_permutation import permute


class BasicRecursionsTest(TestCase):
    def test(self):
        self.assertEqual(sorted(permute('a')), sorted(['a']))
        self.assertEqual(sorted(permute('ab')), sorted(['ab', 'ba']))
        self.assertEqual(sorted(permute('abc')),
                         sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        self.assertEqual(sorted(permute('dog')),
                         sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']))
