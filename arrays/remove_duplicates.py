"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new lenth.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return lenth = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned lenth.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return lenth = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned lenth.
"""


def remove_duplicates(nums):
    lenth = 0
    if len(nums) == 0:
        return lenth
    for i in range(1, len(nums)):
        if nums[lenth] < nums[i]:
            lenth += 1
            nums[lenth] = nums[i]
    return lenth + 1


remove_duplicates([1, 1, 2])
