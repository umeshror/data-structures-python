"""
Given a string of opening and closing parentheses, check whether its balanced.
 We have 3 types of parentheses: round brackets: (), square brackets: [], and
 curly brackets: {}. Assume that the string doesn't contain any other character
 than these, no spaces words or numbers. As a reminder, balanced parentheses
 require every opening parenthesis to be closed in the reverse order opened.
For example ([]) is balanced but ([)] is not.
"""


def balance_check(s):
    if len(s) == 0:
        return False

    opening_brackets = ["(", "[", "{"]

    mathches = (("(", ")"), ("[", "]"), ("{", "}"))

    stack = []

    for paren in s:
        if paren in opening_brackets:
            stack.append(paren)
        else:
            # char is closing one
            if len(stack) == 0:
                return False
            # get the last open char added using stack
            last_open_paren = stack.pop()

            if (last_open_paren, paren) not in mathches:
                return False

    return len(stack) == 0
