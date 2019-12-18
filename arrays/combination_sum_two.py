"""
Given a collection of candidate numbers (nums) and a target number (target),
 find all unique combinations in nums where the candidate numbers sums to target.

Each number in nums may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Input: nums = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Input: nums = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


def combination_sum(candidates, target):
    """
    :param nums: List of +ve ints: [10,1,2,7,6,1,5]
    :param target: INT: 8
    """
    candidates.sort()  # [1, 1, 2, 5, 6, 7, 10]
    out = []
    dfs(candidates, target, 0, [], out)
    return out


def dfs(candidates, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return  # backtracking
    for i in range(index, len(candidates)):
        if i > index and candidates[i] == candidates[i - 1]:
            continue
        dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], res)
print(combination_sum([10,1,2,7,6,1,5], 8))
print(combination_sum([2,5,2,1,2], 5))
