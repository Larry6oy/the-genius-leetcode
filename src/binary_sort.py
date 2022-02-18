from operator import index
from typing import List
class Solution:    
    def sortArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size == 0:
            return nums
        l = []
        m = []
        p = nums[0]
        for n in range(1, size):
            num = nums[n]
            if num < p:
                l.append(num)
            else:
                m.append(num)
        return self.sortArray(l) + [p] + self.sortArray(m)

example = Solution()


print(example.sortArray([4, 3, 2, 1])) # => [1, 2, 3, 4]
print(example.sortArray([2, 4, 3, 1])) # => [1, 2, 3, 4]
print(example.sortArray([3, 1, 2, 4])) # => [1, 2, 3, 4]
print(example.sortArray([3, 2, 1, 4])) # => [1, 2, 3, 4]

