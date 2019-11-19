"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


def is_palindrome_sol1(number):
    """
    :param number: integer : -123
    :return: True/False
    """
    is_negative = number < 0
    if is_negative:
        number = -1 * number
    reverse = 0
    tmp = number
    while number:
        reverse = reverse * 10 + number % 10
        number = number // 10
    if is_negative:
        reverse *= -1
    return reverse == tmp


print(is_palindrome_sol1(-121))
print(is_palindrome_sol1(-122))
print(is_palindrome_sol1(122))
print(is_palindrome_sol1(121))

def is_palindrome_sol2(number):
    """
    :param number: integer : -123
    :return: True/False
    """
    return str(number) == str(number)[::-1]

print(is_palindrome_sol2(-121))
print(is_palindrome_sol2(-122))
print(is_palindrome_sol2(122))
print(is_palindrome_sol2(121))
