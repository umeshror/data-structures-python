def bubble_sort_sol1(arr):
    i = 0
    while i < len(arr):
        j = 0
        while j < len(arr) -1:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

            j += 1
        i += 1
    return arr

print bubble_sort_sol1([12, 43, 123, -34, 0, 1, 58, 2, 46, 89, 2, 12, 46, 768, 23])
