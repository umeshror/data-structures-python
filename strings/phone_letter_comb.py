"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
 Note that 1 does not map to any letters.

 1   2    3
    abc  def
 4   5    6
ghi jkl  mno
 7    8    9
pqrs tuv  wxyy


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


def find_combinations(digits):
    """
    Apply Backtracking
    Take 1 char and do recursion to its end
    Apply this to all chars numbers.
    """

    NUM_MAP = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    if not digits or digits in "01" or not digits.isdigit():
        return []
    out = []

    def combine_chars(strng_out, remain_digits):
        if not remain_digits:
            # reached last digit add string to out
            out.append(strng_out)
            return []
        current_digit = remain_digits[0]
        for char in NUM_MAP[current_digit]:
            # add current char to the strng calculated so far
            strng = strng_out + char
            # get the remain strng for leftover digits
            combine_chars(strng, remain_digits[1:])


    combine_chars("", digits)
    return out


print(find_combinations("1"))
