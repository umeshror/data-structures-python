def length_of_longest_substring(s):
    """
    :type s: str
    :rtype: int
    """
    substring = ""
    longest_sub = ""
    for char in s:
        if char not in substring:
            substring += char
        else:
            # abcbad ==>[a,c,ad]==>ad + char
            substring = substring.split(char)[-1] + char
        if len(longest_sub) < len(substring):
            longest_sub = substring
    return len(longest_sub)


print length_of_longest_substring("abcabcbb")
print length_of_longest_substring(" ")
print length_of_longest_substring("dvdf")
print length_of_longest_substring("ynyo")
