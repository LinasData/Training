from typing import List


def binary_search(list_of_nums: List[int], needed_num: int):

    length_of_list = len(list_of_nums)
    middle_index = length_of_list // 2
    middle_num = list_of_nums[middle_index]


    if middle_num == needed_num:
        return "Found out number"
    elif middle_num < needed_num:
        print("higher")
        return binary_search(list_of_nums[middle_index:], needed_num)
    elif middle_num > needed_num:
        print("lower")
        return binary_search(list_of_nums[:middle_index], needed_num)
    else:
        return "Not Found"
