"""
Given a string s, find the longest palindromic substring in s.
 You may assume that the maximum length of s is 1000.
"""
class Solution(object):
    def longest_palindrome(self, s):
        longest = ""
        for i in range(len(s)):
            # odd case, like "aba"
            odd = self.longest_at_ind(s, i, i)
            if len(odd) > len(longest):
                longest = odd
            # even case, like "abba"
            even = self.longest_at_ind(s, i, i + 1)
            if len(even) > len(longest):
                longest = even
        return longest

    # from inner to outer
    def longest_at_ind(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]


s = Solution()
print s.longest_palindrome('babadasccascaaaaaabbbdfv')
