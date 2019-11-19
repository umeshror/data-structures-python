"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make th0 is conversion given a number of rows:

string convert(string s, int numRows);

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

"""
import collections


def zigzag_sol1(s, num_rows):
    char_map = collections.defaultdict(str)
    row = 0
    step = 1
    for ind, char in enumerate(s, 1):
        # increment/decrement row by step,
        # increment until reaches to num_rows then decrement until reaches to first row
        row = row + step
        char_map[row] += char
        if row == num_rows:
            step = -1
        if row == 1:
            step = 1
    out = ""
    for chars in char_map.values():
        out += chars
    return out


print(zigzag_sol1("PAYPALISHIRING", 4))


def zigzag_sol2(s, num_rows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """

    if num_rows == 1 or num_rows >= len(s):
        return s
    row = 0
    step = 0
    out = [""] * num_rows
    for char in s:
        # increment/decrement row by step,
        # increment until reaches to num_rows then decrement until reaches to first row
        out[row] += char
        if row == num_rows - 1:
            step = -1
        elif row == 0:
            step = 1
        row += step
    return "".join(out)

print(zigzag_sol2("PAYPALISHIRING", 4))
