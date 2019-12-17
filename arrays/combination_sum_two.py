"""
Given a collection of candidate numbers (candidates) and a target number (target),
 find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


def combination_sum(nums, target):
    """
    :param nums: List of +ve ints: [10,1,2,7,6,1,5]
    :param target: INT: 8
    """
    nums.sort()  # [1, 1, 2, 5, 6, 7, 10]
    out = []
    dfs(nums, 0, target, [], out)
    return out

def dfs(nums, curr_ind, target, path, out):
    """
    :param nums:  List of +ve ints
    :param curr_ind: curr_ind in nums where the pointer is
    :param target: Target to achieve in this iteration
    :param path: Path found till now to achieve target
    :param out: Total paths found for achieving target
    :return:
    """
    if target < 0:
        return
    if target == 0:
        out.append(path)

    for i, num in enumerate(nums[curr_ind:]):
        if i > curr_ind and nums[i-1] == nums[i]:
            continue
        dfs(nums[curr_ind:], i+1, target - num, path + [num], out)

print(combination_sum([10,1,2,7,6,1,5], 8))
#[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
