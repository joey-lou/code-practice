import numpy as np


def partition(arr, low, high):
    # lomuto scheme
    i = low
    pivot = high
    for j in range(low, high):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[pivot] = arr[pivot], arr[i]
    return i


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


print("lomuto")
arr = np.random.randint(1, 100, 100)
quicksort(arr, 0, len(arr) - 1)
print(arr)


def partition(arr, low, high):
    # Hoare_partition_scheme
    pivot = low + (high - low) // 2
    i, j = low, high
    while True:
        while arr[i] < arr[pivot]:
            i += 1
        while arr[j] > arr[pivot]:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort_dumb(array):
    if len(array) < 2:
        return array
    pivot = len(array) // 2
    pivot_val = array[pivot]
    left_arr = []
    right_arr = []
    mid_arr = []
    for num in array:
        if num < pivot_val:
            left_arr.append(num)
        elif num == pivot_val:
            mid_arr.append(num)
        else:
            right_arr.append(num)
    return quick_sort_dumb(left_arr) + mid_arr + quick_sort_dumb(right_arr)


print("Quick sort dumb")
arr = np.random.randint(1, 100, 100)
print(quick_sort_dumb(arr))


def mergesort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left_arr = mergesort(arr[:mid])
    right_arr = mergesort(arr[mid:])

    merge_arr = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            merge_arr.append(left_arr[i])
            i += 1
        else:
            merge_arr.append(right_arr[j])
            j += 1
    merge_arr.extend(left_arr[i:])
    merge_arr.extend(right_arr[j:])
    return merge_arr


print("merge")
arr = np.random.randint(1, 100, 100)
print(mergesort(arr))
