import random

input_array = random.sample(range(1, 999), 20)


def sort(array: list) -> list:
    """
    Bubble Sort algorithm implementation.

    Args:
        array (list): list of random numbers

    Returns:
        list: sorted array
    """
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]

            return sort(array)

    return array


sorted_array = sort(input_array)

if sorted(sorted_array):
    print(f"Sorted array: {sorted_array}")
else:
    print("Unsorted")
