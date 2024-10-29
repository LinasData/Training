import random

input_array = random.sample(range(1, 999), 20)


def merge_sort(arr: list) -> list:
    """
    Sorts a list of elements using the merge sort algorithm.

    This function recursively divides the list into halves,
    sorts each half, and then merges them back together.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list of elements.

    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: list, right: list) -> list:
    """
    Merges two sorted lists into a single sorted list.

    This function combines the elements from both lists
    while maintaining their sorted order.

    Args:
        left (list): The first sorted list of elements.
        right (list): The second sorted list of elements.

    Returns:
        list: A new list containing all elements from both
        input lists in sorted order.

    Examples:
        >>> merge([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
        >>> merge([], [1, 2, 3])
        [1, 2, 3]
    """
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


sorted_array = merge_sort(input_array)

if sorted(sorted_array):
    print(f"Sorted array: {sorted_array}")
else:
    print("Unsorted")
