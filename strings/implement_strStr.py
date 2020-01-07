"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


def strStr(haystack, needle):
    """
    KMP solution
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not haystack and not needle:
        return 0

    if not needle:
        return 0

    prefix_arr = [0]
    j, i, m, n = 0, 1, len(haystack), len(needle)
    while len(prefix_arr) != n:
        if needle[i] != needle[j] and j == 0:
            prefix_arr.append(0)
            i += 1
        elif needle[i] != needle[j] and j != 0:
            j = prefix_arr[j - 1]
        else:
            prefix_arr.append(j + 1)
            i += 1
            j += 1


    p1, p2 = 0, 0
    while p1 < m:
        if haystack[p1] == needle[p2]:
            p1 += 1
            p2 += 1

        if p2 == n:
            return p1 - p2
        elif p1 < m and haystack[p1] != needle[p2]:
            if p2 == 0:
                p1 += 1
            else:
                p2 = prefix_arr[p2 - 1]
    return -1

print(strStr('hello', 'll'))
