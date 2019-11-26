"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.


Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""
import collections


def three_sum_sol1(nums):
    positives = collections.defaultdict(int)
    negatives = collections.defaultdict(int)
    zero = 0
    for num in nums:
        if num > 0:
            positives[num] += 1
        elif num == 0:
            zero += 1
        else:
            negatives[num] += 1
    out = []
    if zero >= 3:
        out.append((0, 0, 0))

    for num in positives:
        # for (-1, 0, 1)
        if zero and -num in negatives:
            out.append((-num, 0, num))
        # for (-2, 1, 1)
        if -2 * num in negatives and positives[num] > 1:
            out.append((-2 * num, num, num))
        pos_num = num / 2.0
        # int(1.5) != 1 but int(1.0) == 1
        if int(pos_num) != pos_num:
            continue
        pos_num = int(pos_num)
        # for (-2, -2, 4)
        if -pos_num in negatives and negatives[-pos_num] > 1:
            out.append((-pos_num, -pos_num, num))

    return out


# print(three_sum( [-1, 0, 1, 2, -1, -4]))
# print(three_sum( [0,0,0]))
# print(three_sum([-1, 0, 1, 2, -1, -4]))
# print(three_sum([0, 0]))
# print(three_sum([0, 0, 0, 0]))
print(three_sum([3, 0, -2, -1, 1, 2]))
# [[-2,-1,3],[-2,0,2],[-1,0,1]]