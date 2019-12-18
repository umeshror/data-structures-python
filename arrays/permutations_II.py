"""
Given a collection of numbers that might contain duplicates,
 return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


def find_unique_permutations(arr):
    out = []
    arr.sort()
    dfs(arr, [], out)
    return out


def dfs(arr, path, out):
    """
    :param arr: List of integers
    :param path: Path reached till now
    :param out: Response
    """
    if not arr:
        out.append(path)
        return

    for i in range(len(arr)):
        # skip to next element as its already handled
        if i > 0 and arr[i] == arr[i-1]:
            continue
        dfs(arr[:i] + arr[i + 1:], path + [arr[i]], out)
print(find_unique_permutations([1, 1, 2]))
