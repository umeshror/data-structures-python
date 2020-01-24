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


def binary_search_left(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) / 2
        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return left


def binary_search_right(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) / 2
        if target >= nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return right


def search_range_sol1(nums, target):
    left, right = binary_search_left(nums, target), binary_search_right(nums, target)
    return (left, right) if left <= right else [-1, -1]


print(search_range_sol1([5, 7, 7, 8, 8, 10], 8))
print(search_range_sol1([5, 7, 7, 8, 8, 10], 6))


def search_range_sol2(nums, target):
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


print(search_range_sol2([5, 7, 7, 8, 8, 10], 8))
print(search_range_sol2([5, 7, 7, 8, 8, 10], 6))
