"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Input: dividend = 10, divisor = 3
Output: 3

Input: dividend = 7, divisor = -3
Output: -2

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
"""


def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    sign = 1
    if 0 in [dividend, divisor]:
        return 0

    if dividend < 0 < divisor or divisor < 0 < dividend:
        sign = -1

    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        tmp = divisor
        val = 1
        while dividend >= tmp:
            res += val
            dividend -= tmp
            tmp += tmp
            val += val
    return sign * res


print(divide(-2147483648, -1))
print(divide(-1, -1))
print(divide(10, 3))
print(divide(7, -3))
