def selection_sort_min(arr):
    for i in range(len(arr)):
        min_value_ind = i

        for j in range(i + 1, len(arr)):

            if arr[j] < arr[min_value_ind]:
                min_value_ind = j
            j += 1
        arr[i], arr[min_value_ind] = arr[min_value_ind], arr[i]
    return arr


print(selection_sort_min([2, 324, 6]))


def selection_sort_max(arr):
    # For every slot in array
    for i in range(len(arr) - 1, 0, -1):
        max_value_ind = 0

        # For every set of 0 to i+1
        for j in range(1, i + 1):
            # Set maximum's j
            if arr[j] > arr[max_value_ind]:
                max_value_ind = j

        temp = arr[i]
        arr[i] = arr[max_value_ind]
        arr[max_value_ind] = temp
    return arr


print(selection_sort_max([2, 324, 6]))


def selection_sort_max_sol2(arr):
    """
    max_ind    2, 324, 6, 22
     2:234     2, 22, 6, 324
     1:22      2, 6, 22, 324
     1:6       2, 6, 22, 324
     0:2       2, 6, 22, 324
    :param arr:
    :return:
    """
    i = 0
    while i < len(arr):
        max_value_ind = 0
        j = 0
        while j < len(arr) - i:
            if arr[j] > arr[max_value_ind]:
                max_value_ind = j
            j += 1
        arr[max_value_ind], arr[j - 1] = arr[j - 1], arr[max_value_ind]

        i += 1
    return arr

print(selection_sort_max_sol2([2, 324, 6, 22]))
