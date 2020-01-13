"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

In case we consider the permutations of {1,2,3} in lexicographical order then they will be
“123, 132, 213, 231, 312, 321”.

S = {1, 2, 3, 4, 5, 6}

123 < 124 < 125 < 126 < 134 < 135 < 136 < 145 < 146 < 156 <
234 < 235 < 236 < 245 < 246 < 256 < 345 < 346 < 356 < 456.

Input   Output
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


def next_permutation(nums):
    """
    :type nums: List[int]
    """
    i = j = len(nums) - 1
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1
    if i == 0:  # nums are in descending order
        nums.reverse()
        return
    k = i - 1  # find the last "ascending" position
    while nums[j] <= nums[k]:
        j -= 1
    nums[k], nums[j] = nums[j], nums[k]
    l, r = k + 1, len(nums) - 1  # reverse the second part
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    return nums


print(next_permutation([1, 2, 3]))
print(next_permutation([2, 1, 3]))
print(next_permutation([3, 2, 1]))


def next_permutation_sol2(nums):
    """
    :type nums: List[int]
    """
    # Use two-pointers: two pointers start from back
    # first pointer j stop at descending point
    # second pointer i stop at value > nums[j]
    # swap and sort rest
    if not nums:
        return None
    i = len(nums) - 1
    j = -1  # j is set to -1 for case `4321`, so need to reverse all in following step
    while i > 0:
        if nums[i - 1] < nums[i]:  # first one violates the trend
            # 123 => 132,  1234 => 1243
            # j = 1         j =2
            j = i - 1
            break
        i -= 1
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > nums[j]:  #
            nums[i], nums[j] = nums[j], nums[i]  # swap position
            nums[j + 1:] = sorted(nums[j + 1:])  # sort rest
            break
    return nums


print(next_permutation_sol2([1, 2, 3]))
print(next_permutation_sol2([2, 1, 3]))
print(next_permutation_sol2([3, 2, 1]))
