"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note: All given inputs are in lowercase letters a-z.

"""


def longest_common_prefix(strngs):
    if not strngs:
        return ""
    out = strngs[0]
    for strng in strngs[1:]:
        tmp = ""
        for i, char in enumerate(strng[:min(len(out), len(strng))]):
            if char == out[i]:
                tmp += char
            else:
                break
        out = tmp
        if not out:
            break
    return out


print(longest_common_prefix(["flower", "flow", "flight", "flll", ""]))
print(longest_common_prefix([]))
print(longest_common_prefix(["a"]))


def longest_common_prefix_sol2(strngs):
    if not strngs:
        return ""
    if len(strngs) == 1:
        return strngs[0]

    strngs.sort()
    out = ""
    for x, y in zip(strngs[0], strngs[-1]):
        if x == y:
            out += x
        else:
            break
    return out


print(longest_common_prefix_sol2(["flower", "flow", "flight", "flll", ""]))
print(longest_common_prefix_sol2([]))
print(longest_common_prefix_sol2(["a"]))
