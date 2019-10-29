"""
Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 (1,3)
 (2,2)

"""

# solution 1 : O(nlogn)

def pair_sum_sol1(arr, k):
    if len(arr) < 2:
        return
    found = []
    for ind, element in enumerate(arr, 1):
        for item in arr[ind:]:
            if element + item is k:
                found.append((element, item))
    return len(found)
# output 2
# pair_sum_sol1([1, 3, 2, 2], 4)

# solution 2 : O(n)
def pair_sum_sol2(arr, k):
    counter = 0
    lookup = set()
    for element in arr:
        if k - element in lookup:
            counter += 1
        else:
            lookup.add(element)
    return counter

pair_sum_sol2([1, 3, 2, 2], 4)