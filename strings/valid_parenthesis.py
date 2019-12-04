"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
 determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Input: "()"
Output: true

Input: "()[]{}"
Output: true

Input: "(]"
Output: false

Input: "([)]"
Output: false

Input: "{[]}"
Output: true
"""


def valid_parenthesis(strng):
    """
    Looks if strng has valid parenthesis
    :param strng
    :return: True / False
    """
    bracket_map = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    stack = []

    for char in strng:
        # got close bracket add it to stack
        if char in bracket_map:
            stack.append(char)
        else:
            if not stack:
                # got close bracket but stack is empty
                return False
            last_open_bracket = stack.pop()
            # last_open_bracket is not paired with current close bracket
            if char != bracket_map[last_open_bracket]:
                return False
    # found all strngs but stack is still not empty
    if stack:
        return False
    return True


print(valid_parenthesis('{[]}'))
print(valid_parenthesis('()[]{}'))
print(valid_parenthesis('{[]}'))
print(valid_parenthesis('()[]{}'))
print(valid_parenthesis('()[]{]'))
print(valid_parenthesis('()[]{[()]}'))
print(valid_parenthesis('['))
print(valid_parenthesis(']'))
