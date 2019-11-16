from unittest import TestCase

from graph.word_ladder import word_ladder


class WordLadderTest(TestCase):
    def test(self):
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        self.assertEqual(word_ladder("hit", "cog", word_list), 5)
        self.assertEqual(word_ladder("hot", "cog", word_list), 4)
        self.assertEqual(word_ladder("hhh", "cog", word_list), 0)
        self.assertEqual(word_ladder("loh", "lot", word_list), 2)
