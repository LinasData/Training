from typing import List

import big_o


def binary_search(list_of_nums: List[int], needed_num: int, index: int = 0):

    middle_index = len(list_of_nums) // 2
    middle_num = list_of_nums[middle_index]

    print(list_of_nums)
    if middle_num == needed_num:
        return f"Found out number. Position {middle_index + index}"
    elif middle_num > needed_num:
        print("Lower")
        return binary_search(list_of_nums[middle_index:], needed_num, index + 1)
    elif middle_num < needed_num:
        print("Higher")
        return binary_search(list_of_nums[:middle_index], needed_num, index + 1)
    else:
        return "Not Found"

print(binary_search( [13, 11, 10, 7, 4, 3, 1, 0], 7))

# Function to generate test inputs for big_o analysis
def generate_input(n):
    return list(range(n))

best, others = big_o.big_o(binary_search, generate_input)

