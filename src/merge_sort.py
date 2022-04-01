

from typing import List


class Solution:    
    def mergeSort(self, nums: List[int]) -> List[int]:
        r = len(nums)
        l = 0
        return self.mergeSortInternal(nums, l, r)


    def mergeSortInternal(self, nums: List[int], s: int, e: int):
        if s == e:
            return []
        elif e == s+1:
            return [nums[s]]
        else:
            m = int((s+e)/2)
            left = self.mergeSortInternal(nums, s, m)
            right = self.mergeSortInternal(nums, m, e)
            return self.mergeTwoArray(left, right)

    def mergeTwoArray(self, n1: List[int], n2:List[int]):
        result = []
        p1 = 0
        p2 = 0

        while(p1<len(n1) and p2<len(n2)):
            v1 = n1[p1]
            v2 = n2[p2]
            if(v1 < v2):
                result.append(v1)
                p1 = p1+1
            else:
                result.append(v2)
                p2 = p2+1
        while(p1<len(n1)):
            result.append(n1[p1])
            p1 = p1+1
        while(p2<len(n2)):
            result.append(n2[p2])
            p2 = p2+1
        return result
        
        




example = Solution()
print(example.mergeSort([]))
print(example.mergeSort([1]))
print(example.mergeSort([2, 1]))
print(example.mergeSort([3, 1, 2]))
print(example.mergeSort([4, 3, 1, 2]))
print(example.mergeSort([1, 3, 2, 4, 5])) # => [1, 2, 3, 4, 5]
print(example.mergeSort([4, 5, 3, 2, 1])) # => [1, 2, 3, 4, 5]
print(example.mergeSort([3, 1, 5, 2, 6])) # => [1, 2, 3, 5, 6]
print(example.mergeSort([1, 3, 2, 5])) # => [1, 2, 3, 5]
print(example.mergeSort([1, 5, 3])) # => [1, 3, 5]
print(example.mergeSort([1, 3, 4, 3])) # => [1, 3, 3, 4]
