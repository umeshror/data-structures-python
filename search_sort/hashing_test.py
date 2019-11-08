from unittest import TestCase

from search_sort.hashing import HashTable


class HashTableTest(TestCase):
    def test(self):
        hash_table = HashTable(5)
        hash_table[1] = 'one'
        hash_table[2] = 'two'
        self.assertEqual(hash_table[1], "one")
        self.assertEqual(hash_table[2], "two")
        self.assertEqual(hash_table[4], None)
