"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II.
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Input: 3
Output: "III"

Input: 4
Output: "IV"

Input: 9
Output: "IX"

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
from collections import OrderedDict


def integer_to_roman(number):
    roman_map = OrderedDict([(1000, 'M'),
                             (900, 'CM'),
                             (500, 'D'),
                             (400, 'CD'),
                             (100, 'C'),
                             (90, 'XC'),
                             (50, 'L'),
                             (40, 'XL'),
                             (10, 'X'),
                             (9, 'IX'),
                             (5, 'V'),
                             (4, 'IV'),
                             (1, 'I')
                             ])
    out = ""
    for key in roman_map:
        while number >= key:
            out += roman_map[key]
            number -= key
    return out


print(integer_to_roman(3))
print(integer_to_roman(4))
print(integer_to_roman(8))
print(integer_to_roman(58))


def integer_to_roman_sol2(num):
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    first_digit = num // 1000
    second_digit = (num % 1000) // 100
    third_digit = (num % 100) // 10
    fourth_digit = num % 10
    return M[first_digit] + C[second_digit] + X[third_digit] + I[fourth_digit]


print(integer_to_roman_sol2(3))
print(integer_to_roman_sol2(4))
print(integer_to_roman_sol2(8))
print(integer_to_roman_sol2(58))
print(integer_to_roman_sol2(588))
print(integer_to_roman_sol2(3999))
