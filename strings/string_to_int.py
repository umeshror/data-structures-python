"""
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
 Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as
  possible, and interprets them as a numerical value.

Input: "42"
Output: 42

Input: "   -42"
Output: -42

Input: "4193 with words"
Output: 4193

Input: "words and 987"
Output: 0

Input: "-91283472332"
Output: -2147483648

"""
def strng_to_int(strng):
    strng = strng.strip()
    if len(strng) == 0:
        return 0
    out = "0"
    i = 0
    if strng[0] in "+-":
        out = strng[0]
        i = 1
    for char in strng[i:]:
        if char.isdigit():
            out += char
        else:
            break
    # if out is + or -
    if len(out) == 1:
        return 0
    out = int(out)
    if (out.bit_length() >= 32):
        return (2 ** 31 - 1) if out > 0 else -2 ** 31
    return out
print(strng_to_int( "   -42l knj;nuvk"))
print(strng_to_int("+"))
print(strng_to_int(""))
print(strng_to_int("+-"))