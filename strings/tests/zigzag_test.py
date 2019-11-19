from unittest import TestCase

from strings.zigzag import zigzag_sol1, zigzag_sol2


class ZigZagTest(TestCase):
    def test_sol1(self):
        self.assertEqual(zigzag_sol1("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
        self.assertEqual(zigzag_sol1("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(zigzag_sol1("PAYPALISHIRING", 2), "PYAIHRNAPLSIIG")
        self.assertEqual(zigzag_sol1("PAYPALISHIRING", 1), "PAYPALISHIRING")
        self.assertEqual(zigzag_sol1("AB", 1), "AB")
        self.assertEqual(zigzag_sol1("ABC", 2), "ACB")
        self.assertEqual(zigzag_sol1("AB", 3), "AB")
        self.assertEqual(zigzag_sol1("A", 3), "A")
        self.assertEqual(zigzag_sol1("", 3), "")

    def test_sol2(self):
        self.assertEqual(zigzag_sol2("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
        self.assertEqual(zigzag_sol2("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(zigzag_sol2("PAYPALISHIRING", 2), "PYAIHRNAPLSIIG")
        self.assertEqual(zigzag_sol2("PAYPALISHIRING", 1), "PAYPALISHIRING")
        self.assertEqual(zigzag_sol2("AB", 1), "AB")
        self.assertEqual(zigzag_sol2("ABC", 2), "ACB")
        self.assertEqual(zigzag_sol2("AB", 3), "AB")
        self.assertEqual(zigzag_sol2("A", 3), "A")
        self.assertEqual(zigzag_sol2("", 3), "")
