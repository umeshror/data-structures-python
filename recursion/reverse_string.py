"""
Reverse a string using recursion.
Do not slice (e.g. string[::-1]) or use iteration, there must be a recursive call for the function
reverse('hello world')
'dlrow olleh'
"""


def reverse_string(s):
    """
    e.g Hello World

    reverse(s[1:]) + s[0]
    reverse(s[1:]) + H
    reverse(s[1:]) + e + H
    reverse(s[1:]) + l + e + H
    .
    .
    .
    """
    # Base Case
    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]


print(reverse_string('hello world'))
