from typing import List


class Solution:
    def partition(self, nums: List[int], start : int, end: int) -> List[int]:
        p = end
        j = start
        i = start-1
        while j < end:
            if nums[j] < nums[p]:
                i = i+1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            j = j+1
        temp = nums[p]
        nums[p] = nums[i+1]
        nums[i+1] = temp
        while p < start:
            self.partition(nums, start, p)
        while p < end:
            self.partition(nums, p, end)
        return nums
    def quickSort(self, nums: List[int]) -> List[int]:
       self.partition(nums, 0, len(nums)-1)
       return nums

example = Solution()       




print(example.partition([10, 80, 30, 90, 40, 50, 70], 0, 6)) # => [10, 30, 40, 50, 70, 90, 80]
print(example.quickSort([10, 80, 30, 90, 40, 50, 70])) # => [10, 30, 40, 50, 70, 80, 90]