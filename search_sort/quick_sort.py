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


def partition_sol_2(array, start_ind, end_ind):
    pivot_ind = start_ind
    for i in xrange(start_ind+1, end_ind+1):
        if arr[i] <= array[start_ind]:
            pivot_ind += 1
            array[i], array[pivot_ind] = array[pivot_ind], array[i]
    array[pivot_ind], array[start_ind] = array[start_ind], array[pivot_ind]
    return pivot_ind



def quick_sort_sol2(array, start_ind=0, end_ind=None):
    if end_ind is None:
        end_ind = len(array) - 1
    if start_ind >= end_ind:
        return
    pivot_ind = partition_sol_2(array, start_ind, end_ind)
    quick_sort_sol2(array, start_ind, pivot_ind-1)
    quick_sort_sol2(array, pivot_ind+1, end_ind)
    return array

print quick_sort_sol2(arr)
