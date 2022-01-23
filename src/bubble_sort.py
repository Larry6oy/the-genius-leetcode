from typing import List


class Solution:
    def single_sort(self, nums: List[int], size: int) -> List[int]:
        for c in range(0, size-1):
            c2 = c+1
            if nums[c] > nums[c2]:
                temp = nums[c]
                nums[c] = nums[c2]
                nums[c2] = temp
        return nums

        
    def complete_sort(self, nums: List[int]) -> List[int]:
        for c in range(1, len(nums)):
            step = len(nums)-c+1
            nums = self.single_sort(nums, step)
        return nums


example = Solution()


print("single sort:")
print(example.single_sort([4, 3, 2, 1], 4)) # => [3, 2, 1, 4]
print(example.single_sort([2, 4, 3, 1], 4)) # => [2, 3, 1, 4]
print(example.single_sort([3, 1, 2, 4], 4)) # => [1, 2, 3, 4]
print(example.single_sort([3, 2, 1, 4], 4)) # => [2, 1, 3, 4]
print("")

print("complete sort:")
print(example.complete_sort([4, 3, 2, 1])) # => [1, 2, 3, 4]
print(example.complete_sort([2, 4, 3, 1])) # => [1, 2, 3, 4]
print(example.complete_sort([3, 1, 2, 4])) # => [1, 2, 3, 4]
print(example.complete_sort([3, 2, 1, 4])) # => [1, 2, 3, 4]