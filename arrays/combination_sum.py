"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


def combination_sum(candidates, target):
    """
    :param candidates: List(Pos_int): [2,3,5]
    :param target: Int: 8
    :return: List of List
    """
    res = []
    # get the set of candidates to avoid loop on duplicate items
    candidates = set(candidates)
    dfs(candidates, -1, target, [], res)
    return res


def dfs(nums, prev_num, target, path, res):
    if target < 0:
        return
    if target == 0:
        res.append(path)
        return
    for num in nums:
        # this num should be equal to or less than prev_num
        # this will avoid considering past elemets when moving forward
        # for unique combination's
        if num >= prev_num:
            dfs(nums, num, target - num, path + [num], res)


print(combination_sum([2, 3, 5], 8))
