import random
import time

# create list with 300 elements
data = []
for i in range(300):
    data.append(random.randint(1, 1000))


# Selection Sort
def selection_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        temp = a[i]
        a[i] = a[min_index]
        a[min_index] = temp
    return a


# Bubble Sort
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
    return a


# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Selection Sort Test
start = time.time()
final_selection_sort = selection_sort(data) 
end = time.time()

print("Selection Sort Result:")
print(f'{final_selection_sort}\n')
print("Time:", end - start, "\n")


# Bubble Sort Test
start = time.time()
final_bubble_sort = bubble_sort(data)
end = time.time()

print("Bubble Sort Result:")
print(f'{final_bubble_sort}\n')
print("Time:", end - start, "\n")


# Merge Sort Test
start = time.time()
final_merge_sort = merge_sort(data)
end = time.time()

print("Merge Sort Result:")
print(print(f'{final_merge_sort}\n'))
print("Time:", end - start)