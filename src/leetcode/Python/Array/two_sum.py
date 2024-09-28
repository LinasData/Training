from typing import List


# First way
class Solution:
    def twoSum(self, nums: List[int], target: int, first_index:int = 0) -> List[int]:

        this = nums[0]
        for index, _ in enumerate(nums):
            next_index = index + 1

            if len(nums) > next_index:
                next = nums[next_index]
                answer = this + next

                if answer == target:
                    return [first_index, next_index+first_index]
                continue

            new_nums = nums[1:]
            first_index +=1

            return self.twoSum(new_nums, target, first_index)

# Second way - more efficient with hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if nums[i] in numMap:
                return [numMap[nums[i]], i ]
            numMap[compliment] = i
        return []