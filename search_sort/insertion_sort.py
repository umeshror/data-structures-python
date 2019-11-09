def insertion_sort_sol1(arr):
    """
    :param arr: unsorted array e.g. [43, 1, 2]
    :return: sorted array [1, 2, 43]
    """
    for i in range(1, len(arr)):
        current_value = arr[i]

        for j in range(i, 0, -1):
            if current_value < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

print(insertion_sort_sol1([43, 1, 2, 0,12,121,-12]))
