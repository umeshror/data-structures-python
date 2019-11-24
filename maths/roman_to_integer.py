"""
Input: "III"
Output: 3

Input: "IV"
Output: 4

Input: "LVIII"
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""


def roman_to_int(roman_num):
    """
    Get the last char value.
    Compare this value to second last.
    IF greater current_val >=  last_value then add to out
    else substract
    :param roman_num:  Roman str e.g.MCMXCIV
    :return: INT 194
    """
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    last_value = symbols[roman_num[-1]]
    int_num = last_value

    for char in reversed(roman_num[:-1]):
        current_val = symbols[char]
        if current_val >= last_value:
            int_num += current_val
        else:
            int_num -= current_val
        last_value = current_val

    return int_num


print(roman_to_int("III"))
print(roman_to_int("IX"))
print(roman_to_int("MCMXCIV"))
