"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


def find_permutations(arr):
    out = []
    arr.sort()
    dfs(arr, [], out)
    return out


def dfs(arr, path, out):
    """
    :param arr: List of integers
    :param path: Path reached till now
    :param out: Reponse
    """
    if not arr:
        out.append(path)
        return

    for i in range(len(arr)):
        dfs(arr[:i] + arr[i + 1:], path + [arr[i]], out)


print(find_permutations([1, 2, 3]))
