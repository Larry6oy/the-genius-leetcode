from typing import List

import test_framework


def reverse_sort_single(nums: List[int], size: int) -> List[int]:
    for c in range(0, size-1):
        c2 = c+1
        if nums[c] < nums[c2]:
            temp = nums[c]
            nums[c] = nums[c2]
            nums[c2] = temp

    return nums

def reverse_sort(nums: List[int]) -> List[int]:
    for c in range(1, len(nums)):
        step = len(nums)-c+1
        nums = reverse_sort_single(nums, step)
    return nums

print("single reverse sort:")
print(reverse_sort_single([1, 2, 3, 4], 4)) # => [1, 3, 4, 1]
print(reverse_sort_single([2, 4, 3, 1], 4)) # => [4, 3, 2, 1]
print(reverse_sort_single([3, 1, 2, 4], 4)) # => [3, 2, 4, 1]
print(reverse_sort_single([3, 2, 1, 4], 4)) # => [3, 2, 4, 1]
print("")

print("complete reverse sort:")
print(reverse_sort([1, 2, 3, 4])) # => [4, 3, 2, 1]
print(reverse_sort([2, 4, 3, 1])) # => [4, 3, 2, 1]
print(reverse_sort([3, 1, 2, 4])) # => [4, 3, 2, 1]
print(reverse_sort([3, 2, 1, 4])) # => [4, 3, 2, 1]
