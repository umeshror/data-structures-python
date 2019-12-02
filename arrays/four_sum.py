"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d
 in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.


Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


def four_sum(nums, target):
    """
    :param nums: <Arr> of intergers
    :param target: <Int> Target sum
    :return: [[]] List of lists
    """
    if len(nums) < 4:
        return []
    out = set()
    nums = sorted(nums)
    # fixed first pointer
    for i in range(len(nums) - 3):
        first_num = nums[i]
        # second first pointer
        for j in range(i + 1, len(nums) - 2):
            second_num = nums[j]
            right_ind = j + 1
            left_ind = len(nums) - 1
            # moved remaining pointers
            while right_ind < left_ind:
                # get current sum for all targets
                cur_target = first_num + second_num + nums[right_ind] + nums[left_ind]
                if cur_target == target:
                    out.add((first_num, second_num, nums[right_ind], nums[left_ind]))
                    right_ind += 1
                # if current sum is less than target then move
                # right ind as we want to increase the sum
                elif cur_target < target:
                    right_ind += 1
                else:
                    left_ind -= 1
    return list(out)


print(four_sum([1, 0, -1, 0, -2, 2], 2))
print(four_sum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
