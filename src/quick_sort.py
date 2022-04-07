from random import randrange
from typing import List


class Solution:
    def partition(self, nums: List[int], start : int, end: int) -> List[int]:

        if start >= end:
            return

        p = randrange(0, end)
        j = start
        i = start-1


        while j < end:
            if nums[j] <= nums[p]:
                i = i+1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

            j = j+1
        temp = nums[p]
        nums[p] = nums[i+1]
        nums[i+1] = temp
        p = i+1
        self.partition(nums, start, p-1)
        self.partition(nums, p+1, end)

    def quickSort(self, nums: List[int]) -> List[int]:
        if len(nums) > 0:
            self.partition(nums, 0, len(nums)-1)
        return nums

example = Solution()       




#print(example.partition([10, 80, 30, 90, 40, 50, 70], 0, 6)) # => [10, 30, 40, 50, 70, 80, 90]
print(example.quickSort([10, 80, 30, 90, 40, 50, 70])) # => [10, 30, 40, 50, 70, 80, 90]
print(example.quickSort([])) # => []
print(example.quickSort([3])) # => [3]
print(example.quickSort([3, 1, 3, 40, 5])) # => [1, 3, 3, 5, 40]
print(example.quickSort([3, 1, 3])) # => [1, 3]