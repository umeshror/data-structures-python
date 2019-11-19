"""
Given a 32-bit signed integer, reverse digits of an integer.
"""


def reverse_integer_sol1(number):
    if number >= 2 ** 31 - 1 or number <= -2 ** 31:
        return 0
    is_negative = False
    if number < 0:
        is_negative = True
        number *= -1
    out = 0
    while number != 0:
        out = out * 10 + number % 10
        number = number // 10
    if is_negative:
        out *= -1
    # return 0 if new number is greater than 32-bit signed intege
    if out >= 2 ** 31 - 1 or out <= -2 ** 31:
        return 0
    return out
print(reverse_integer_sol1(123123))
print(reverse_integer_sol1(1534236469))
print(reverse_integer_sol1(-123))