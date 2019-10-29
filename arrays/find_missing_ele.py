"""

Problem
Consider an array of non-negative integers.
A second array is formed by shuffling the elements of the first array and
 deleting a random element. Given these two arrays,
  find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is
 removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

5 is the missing number

"""
import collections


# solution 1
def finder_sol1(arr1, arr2):
    sum = 0
    for ele in arr1:
        sum += ele
    for ele in arr2:
        sum -= ele
    return sum


# solution 1
def finder_sol2(arr1, arr2):
    lookup = collections.defaultdict(int)
    missing_nums = []
    for num in arr2:
        lookup[num] += 1

    for num in arr1:
        if lookup[num] == 0:
            missing_nums.append(num)

    return missing_nums


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 88]
arr2 = [3, 7, 2, 1, 4, 6]
print finder_sol1(arr1, arr2)
print finder_sol2(arr1, arr2)
