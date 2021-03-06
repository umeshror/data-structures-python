"""

Given an unsorted integer array, find the smallest missing positive integer.

Input: [1,2,0]
Output: 3

Input: [3,4,-1,1]
Output: 2

Input: [7,8,9,11,12]
Output: 1

Your algorithm should run in O(n) time and uses constant extra space.
"""


def first_missing_positive_sol1(nums):
    for i in range(len(nums)):
        while 0 <= nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]:
            tmp = nums[i] - 1
            nums[i], nums[tmp] = nums[tmp], nums[i]
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1


# O(nlgn) time
def first_missing_positive_sol2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    res = 1
    for num in nums:
        if num == res:
            res += 1
    return res


# print(first_missing_positive_sol1([1, 2, 0]))
first_missing_positive_sol1([3, 4, -1, 1])

first_missing_positive_sol2([1, 2, 0])
first_missing_positive_sol2([3, 4, -1, 1])
