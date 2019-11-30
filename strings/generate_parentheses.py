"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


def generate_parentheses(n):
    res = []
    def paren(left, right, curr):
        # 'evaluate current string
        # if we are out of brackets to add, we must be at a valid string
        print(left, right, curr)
        if left == 0 and right == 0:
            res.append(curr)
            return

        # recursive call: add either open or close
        # if adding open bracket is valid
        if left > 0:
            # add open bracket, decr count
            paren(left - 1, right, curr + "(")

        # if adding close bracket is valid
        if right > left:
            # add close bracket, decr count
            paren(left, right - 1, curr + ")")

    # end paren()

    paren(n, n, '')

    return res


print(generate_parentheses(2))