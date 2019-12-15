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

    dfs(n, n, '', res)
    return res


def dfs(left, right, curr, res):
    """
    DFS: add either open or close

    2 2 '' []
    1 2 ( []
    0 2 (( []
    0 1 (() []
    0 0 (()) []
    1 1 () ['(())']
    0 1 ()( ['(())']
    0 0 ()() ['(())']
    ret ['()()', '(())']
    """
    # if we are out of brackets to add then return
    if left == 0 and right == 0:
        return res.append(curr)

    # add open bracket, decr left
    if left > 0:
        dfs(left - 1, right, curr + "(", res)

    # add close bracket, decr right
    if right > left:
        dfs(left, right - 1, curr + ")", res)


print(generate_parentheses(2))


