"""
Module for debugging the merge sort algorithm.
"""

from . import rand

def merge_sort(arr):
    """Sorts an array using the merge sort algorithm."""
    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))

def recombine(left_arr, right_arr):
    """Merges two sorted arrays into one sorted array."""
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + i] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[right_index + i] = left_arr[i]

    return merge_arr

if __name__ == "__main__":
    test_array = rand.random_array([None] * 20)
    sorted_array = merge_sort(test_array)
    print(sorted_array)
