"""Sort algorithms"""


def merge_sort(arr):
    comp_n = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            comp_n += 1
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return comp_n


def insertion_sort(arr):
    comp_n = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        comp_n += not (j >= 0 and key < arr[j])
        while j >= 0 and key < arr[j]:
            comp_n += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return comp_n


def selection_sort(arr):
    comp_n = 0
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr) - 1):
            if arr[j] < arr[min_index]:
                min_index = j
            comp_n += 1
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return comp_n


def shell_sort(arr):
    comp_n = 0
    interval = len(arr) // 2
    while interval > 0:
        for i in range(interval, len(arr)):
            temp = arr[i]
            j = i
            comp_n += not (j >= interval and arr[j - interval] > temp)
            while j >= interval and arr[j - interval] > temp:
                comp_n += 1
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp
        interval //= 2
    return comp_n
