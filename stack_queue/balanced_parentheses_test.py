from unittest import TestCase

from stack_queue.balanced_parentheses import balance_check


class TestBalanceCheck(TestCase):
    def test(self):
        self.assertEqual(balance_check('[](){([[[]]])}('), False)
        self.assertEqual(balance_check('[{{{(())}}}]((()))'), True)
        self.assertEqual(balance_check('[[[]])]'), False)
