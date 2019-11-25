from unittest import TestCase

from strings.longest_common_prefix import longest_common_prefix


class StrngToIntTest(TestCase):
    def test(self):
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight", "flll", ""]), "")
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight", "flll"]), "fl")
        self.assertEqual(longest_common_prefix(["flower", "flow"]), "flow")
        self.assertEqual(longest_common_prefix(["flower"]), "flower")
        self.assertEqual(longest_common_prefix(["a"]), "a")
        self.assertEqual(longest_common_prefix([]), "")
