def binary_search(arr, item):
    """
    applies BS algo to find item present in list or not
    :param arr: binary array [1, 2, 3, 4]
    :param item: 3
    :return: True
    """
    if type(arr) != list:
        raise TypeError("Arr should be type of list")
    start_ind = 0
    last_ind = len(arr) - 1

    found = False
    while start_ind <= last_ind and not found:
        mid_ind = (start_ind + last_ind) / 2
        if arr[mid_ind] == item:
            found = True
            break
        elif item < arr[mid_ind]:  # go left
            last_ind = mid_ind - 1
        else:  # go right
            start_ind = mid_ind + 1

    return found


print binary_search([1, 2, 3, 4], 49)
