"""
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
 Return the sum of the three integers. You may assume that each input
 would have exactly one solution.


Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


def three_sum_closet(nums, target):
    """
    1. Sort the numbers in ascending order
    2. Get pivot element, then usr 2 pointers to get next numbers
    3. Check the sum of these number if less than existing out then replace it
    :param nums: <List> : [-1, 2, 1, -4]
    :param target: <Int> : 1
    :return: <Int> : 2
    """
    nums = sorted(nums)

    out = sum(nums[:3])

    for i in range(len(nums)):

        left_ind = i + 1
        right_ind = len(nums) - 1

        while left_ind < right_ind:
            cur_sum = sum([nums[i], nums[left_ind], nums[right_ind]])
            out_to_target = out - target
            curr_to_target = cur_sum - target
            if abs(curr_to_target) < abs(out_to_target):
                # curr_sum is closer to target
                out = cur_sum

            # cur_sum is less than target so keep right ind(large num)
            # and increase left_ind to next(big num)
            if cur_sum < target:
                left_ind += 1
            elif cur_sum > target:
                right_ind -= 1
            # found the exact target break early
            else:
                return out
    return out


print(three_sum_closet([-1, 2, 1, -4], 2))
print(three_sum_closet([-1, 2, 1, -4, 3, 5, 12, 6, 36, 4, 1], 1))
print(three_sum_closet([-1, 2, 1, -4, 3, 5, 12, 6, 36, 4, 1], 2))
