def merge_sort(arr):
    if len(arr) == 1:
        # reached at the last element
        return arr

    middle_ind = len(arr) / 2

    left_half = arr[:middle_ind]
    right_half = arr[middle_ind:]

    sorted_left_half = merge_sort(left_half)
    sorted_right_half = merge_sort(right_half)

    i = 0
    j = 0
    k = 0

    while i < len(sorted_left_half) and j < len(sorted_right_half):
        if sorted_left_half[i] < sorted_right_half[j]:
            arr[k] = sorted_left_half[i]
            i += 1

        else:
            arr[k] = sorted_right_half[j]
            j += 1
        k += 1

    while i < len(sorted_left_half):
        arr[k] = sorted_left_half[i]
        i += 1
        k += 1

    while j < len(sorted_right_half):
        arr[k] = sorted_right_half[j]
        j += 1
        k += 1

    print("Sorted : {}, {} to {}".format(sorted_left_half, sorted_right_half, arr))
    return arr

arr = [11,2,5,4,7,6,8,1,23]
print merge_sort(arr)


