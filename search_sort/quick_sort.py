def quick_sort_sol1(arr):
    if len(arr) <= 1:
        return arr

    less = []
    equal = []
    greater = []
    pivot = arr[0]
    for ele in arr:
        if ele < pivot:
            less.append(ele)
        elif ele == pivot:
            equal.append(ele)
        elif ele > pivot:
            greater.append(ele)
    return quick_sort_sol1(less) + equal + quick_sort_sol1(greater)



arr = [11,2,5,4,7,6,8,1,23]
print quick_sort_sol1(arr)
