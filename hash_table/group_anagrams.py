"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

"""
import collections


def group_anagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    out = collections.defaultdict(list)
    for strng in strs:
        out[''.join(sorted(strng))].append(strng)
    return out.values()


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
