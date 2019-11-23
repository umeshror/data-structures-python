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
def roman_to_int(s):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    last_value = result = symbols[s[-1]]

    for i in reversed(s[:-1]):
        value = symbols[i]
        if value < last_value:
            result -= value
        else:
            result += value
        last_value = value
    return result


print(roman_to_int("III"))
print(roman_to_int("IX"))
print(roman_to_int("MCMXCIV"))
