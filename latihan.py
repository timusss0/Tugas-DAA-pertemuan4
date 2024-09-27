# 1. Swap Function
def swap(x, y):
    var3 = x
    x = y
    y = var3
    return x, y

# Example usage of swap
a = 10
b = 20
a, b = swap(a, b)
print("After swapping:", a, b)

# 2. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Bubble Sort
arr_bubble = [100, 20, 60, 90, 40, 30, 10]
bubble_sort(arr_bubble)
print("Bubble sorted array:", arr_bubble)

# 3. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Insertion Sort
arr_insertion = [89, 12, 57, 16, 25, 11, 75]
insertion_sort(arr_insertion)
print("Insertion sorted array:", arr_insertion)

# 4. Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Selection Sort
arr_selection = [89, 12, 57, 16, 25]
selection_sort(arr_selection)
print("Selection sorted array:", arr_selection)

# 5. Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Linear Search
arr_linear = ['y', 'u', 'i', 'w', 'o', 'a', 'q', 'u', 'j', 'p']
target_linear = 'a'
result_linear = linear_search(arr_linear, target_linear)
print(f"Linear search found '{target_linear}' at index:", result_linear)

# 6. Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Binary Search
arr_binary = sorted(['y', 'u', 'i', 'w', 'o', 'a', 'q', 'u', 'j', 'p'])
target_binary = 'a'
result_binary = binary_search(arr_binary, target_binary)
print(f"Binary search found '{target_binary}' at index:", result_binary)

# 7. Interpolation Search
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        pos = low + ((high - low) // (ord(arr[high]) - ord(arr[low])) * (ord(target) - ord(arr[low])))
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

#Interpolation Search
arr_interpolation = sorted(['y', 'u', 'i', 'w', 'o', 'a', 'q', 'u', 'j', 'p'])
target_interpolation = 'u'
result_interpolation = interpolation_search(arr_interpolation, target_interpolation)
print(f"Interpolation search found '{target_interpolation}' at index:", result_interpolation)
