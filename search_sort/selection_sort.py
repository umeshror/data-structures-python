def selection_sort(arr):
    for i in range(len(arr)):
        min_value_ind = i
        j = 0
        for j in range(i + 1, len(arr) - j):
            if arr[j] < arr[min_value_ind]:
                min_value_ind = j
            j += 1
        arr[i], arr[min_value_ind] = arr[min_value_ind], arr[i]
    return arr


selection_sort([2, 324, 6])
