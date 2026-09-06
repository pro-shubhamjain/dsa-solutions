"""
Problem: Sorting Algorithms
Pattern: Fundamentals (comparison-based sorting)

bubble_sort:    Time O(n^2)     | Space O(1)
selection_sort: Time O(n^2)     | Space O(1)
merge_sort:     Time O(n log n) | Space O(n)

Input:  [100, -40, 500, -124, 0, 21, 7]
Output: [-124, -40, 0, 7, 21, 100, 500]  (same for all three)
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        index_of_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index_of_min]:
                index_of_min = j
        if index_of_min != i:
            arr[i], arr[index_of_min] = arr[index_of_min], arr[i]
    return arr


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    center = len(arr) // 2
    left = arr[:center]
    right = arr[center:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    results = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1
    return results + left[i:] + right[j:]


if __name__ == "__main__":
    print(bubble_sort([100, -40, 500, -124, 0, 21, 7]))
