from unittest import TestCase

from strings.valid_parenthesis import valid_parenthesis


class ValidParenthesisTest(TestCase):
    def test(self):
        self.assertTrue(valid_parenthesis("{}"))
        self.assertTrue(valid_parenthesis("{[([{}])]}{}"))
        self.assertFalse(valid_parenthesis("{[([{}])]}{{"))
        self.assertFalse(valid_parenthesis("{"))
        self.assertFalse(valid_parenthesis("]"))
