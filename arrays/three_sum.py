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


def three_sum_sol2(nums):
    """
    :param nums: [-1, 0, 1, 2, -1, -4]
    :return: [[-1, 0, 1],[-1, -1, 2]]
    """
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
        # [0, 0, 0, 0]
        out.append((0, 0, 0))

    for pos in positives:
        # -1, 0, 1
        if zero and positives[pos] > 0 and -pos in negatives and negatives[-pos] > 0:
            out.append((-pos, 0, pos))

        for neg in negatives:
            # for 2 neg and 1 pos : neg + sec_neg + pos = 0
            # -3 + -1 + 4 = 0 so -3 = -4 + 1
            sec_neg = -(pos + neg)
            # if both neg nos. are same then check if occurrences are more than 1
            if sec_neg == neg and negatives[neg] == 1:
                continue
            # check if sec_neg exist in negatives
            if sec_neg in negatives:
                out.append((min(sec_neg, neg), max(sec_neg, neg), pos))

            # for 2 pos and 1 neg : neg + sec_pos + pos = 0
            # -3 + 1 + 2 = 0 so 3 = -4 + 1
            sec_pos = -(neg + pos)
            if sec_pos == pos and positives[pos] == 1:
                continue

            if sec_pos in positives:
                out.append((neg, min(sec_pos, pos), max(sec_pos, pos)))

    return list(set(out))


print(three_sum_sol2([-1, 0, 1, 2, -1, -4]))
print(three_sum_sol2([0, 0, 0]))
print(three_sum_sol2([-1, 0, 1, 2, -1, -4]))
print(three_sum_sol2([0, 0]))
print(three_sum_sol2([0, 0, 0, 0]))
print(three_sum_sol2([3, 0, -2, -1, 1, 2]))
print(three_sum_sol2([3, -2, 1, 0]))  # []
print(three_sum_sol2([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
