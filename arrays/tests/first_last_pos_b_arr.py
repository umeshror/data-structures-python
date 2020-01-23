"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


def search_range_sol1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    left = -1
    right = -1
    for ind, ele in enumerate(nums):
        if ele > target:
            break
        elif ele == target:
            left = ind
            break
    l = len(nums)
    for ind, ele in enumerate(nums[::-1]):
        if ele < target:
            break
        elif ele == target:
            right = l - ind - 1
            break
    return left, right


print(search_range_sol1([5, 7, 7, 8, 8, 10], 8))
print(search_range_sol1([5, 7, 7, 8, 8, 10], 6))
