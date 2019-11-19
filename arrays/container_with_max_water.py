"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
 n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
  which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


Input: [1,8,6,2,5,4,8,3,7]
Output: 49
The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water the container can contain is 49.
"""


def find_max_area(arr):
    max_area = 0
    for i_ind, i in enumerate(arr):
        for j_ind, j in enumerate(arr[i_ind + 1:], i_ind + 1):
            width = j_ind - i_ind
            height = min(i, j)
            area = width * height
            max_area = max(area, max_area)
    return max_area


print(find_max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(find_max_area([1, 1]))
print(find_max_area([2, 1]))


def find_max_area_sol2(arr):
    max_area = 0
    start = 0
    end = len(arr) - 1
    while start != end:
        s = arr[start]
        e = arr[end]
        height = min(arr[start], arr[end])
        width = end - start
        area = height * width
        max_area = max(max_area, area)
        if arr[start] > arr[end]:
            end -= 1
        else:
            start += 1
    return max_area


print(find_max_area_sol2([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(find_max_area_sol2([1, 1]))
print(find_max_area_sol2([2, 1]))
