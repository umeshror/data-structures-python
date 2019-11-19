"""
Given a 32-bit signed integer, reverse digits of an integer.
"""


def reverse_integer_sol1(number):
    # remainder approach
    if number >= 2 ** 31 - 1 or number <= -2 ** 31:
        return 0
    is_negative = number < 0
    number = abs(number)
    out = 0
    while number != 0:
        out = out * 10 + number % 10
        number = number // 10
    if is_negative:
        out = -out
    # return 0 if new number is greater than 32-bit signed intege
    if out >= 2 ** 31 - 1 or out <= -2 ** 31:
        return 0
    return out


def reverse_integer_sol2(number):
    # convert to str approach
    if number >= 2 ** 31 - 1 or number <= -2 ** 31:
        return 0
    if number > 0:
        number = int(str(number)[::-1])
    else:
        number = -1 * int(str(-1 * number)[::-1])

    if number >= 2 ** 31 - 1 or number <= -2 ** 31:
        return 0
    return number


print(reverse_integer_sol1(123123))
print(reverse_integer_sol1(1534236469))
print(reverse_integer_sol1(-123))
print(reverse_integer_sol2(123123))
print(reverse_integer_sol2(1534236469))
print(reverse_integer_sol2(-123))
