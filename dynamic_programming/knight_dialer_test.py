from unittest import TestCase

from dynamic_programming.knight_dialer import knight_dialer


class KnightDialerTest(TestCase):
    def test(self):
        self.assertEqual(knight_dialer(0), 0)
        self.assertEqual(knight_dialer(1), 10)
        self.assertEqual(knight_dialer(2), 20)
        self.assertEqual(knight_dialer(3), 46)
        self.assertEqual(knight_dialer(4), 104)
        self.assertEqual(knight_dialer(10), 14912)
