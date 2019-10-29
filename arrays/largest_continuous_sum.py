"""
Given an array of integers (positive and negative) find the largest continuous sum.

"""


def large_cont_sum_sol(arr):
    if len(arr) == 0:
        return 0

    max_sum = sum = arr[0]

    for num in arr[1:]:
        # if num is greater than current sum then start fresh
        sum = max(sum + num, num)

        # return max between current sum and max_sum
        max_sum = max(sum, max_sum)
    return max_sum


print large_cont_sum_sol([1, 2, -1, 3, 4, 10, 10, -10, -1])
