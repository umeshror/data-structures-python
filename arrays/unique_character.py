"""
Given a string,determine if it is compreised of all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return false.

"""


def uni_char_sol1(s):
    chars_found = set()
    for char in s:
        if char in chars_found:
            return False
        else:
            chars_found.add(char)
    return True


def uni_char_sol2(s):
    return len(set(s)) == len(s)


print uni_char_sol1("abcde")
print uni_char_sol1("aabcde")
