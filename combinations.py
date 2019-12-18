"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


def combine(n, k):
    """
    :param n: positive int
    :param k: positive int
    :return: List of List
    """
    arr = range(1, n + 1)
    out = []
    dfs(arr, 0, [], out, k)
    return out


def dfs(arr, ind, path, out, k):
    """
    :param arr: List of Int
    :param ind: Current Index
    :param path: Path Visited
    :param out: Response
    :param k: Perms to find
    """
    if len(path) == k:
        out.append(path)
        return
    for i in range(ind, len(arr)):
        dfs(arr, i + 1, path + [arr[i]], out, k)


print(combine(4, 2))
