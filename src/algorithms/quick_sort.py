import random

input_array = random.sample(range(1, 999), 20)


def quicksort(array: list) -> list:
    """
    Quicksort algorithm implementation.

    Args:
        array (list): Initial unsorted array.

    Returns:
        list: Sorted array
    """
    if len(array) < 2:
        return array

    pivot = array[-1]
    less = quicksort([i for i in array[:-1] if i < pivot])
    greater = quicksort([i for i in array[:-1] if i >= pivot])
    return less + [pivot] + greater


sorted_array = quicksort(input_array)

if sorted(sorted_array):
    print(f"Sorted array: {sorted_array}")
else:
    print("Unsorted")
