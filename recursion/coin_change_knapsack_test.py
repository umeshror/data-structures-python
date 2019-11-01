from unittest import TestCase

from recursion.coin_change_knapsack import coin_change


class TestCoinChange(TestCase):
    def test_coin_change(self):
        coins = [1, 5, 10, 25]
        self.assertEqual(coin_change(45, coins), 3)
        self.assertEqual(coin_change(23, coins), 5)
        self.assertEqual(coin_change(74, coins), 8)
