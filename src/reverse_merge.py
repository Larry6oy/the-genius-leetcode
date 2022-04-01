from typing import List

class Solution:
    def reverseMerge(self, nums: List[int]) -> List[int]:
        r = len(nums)
        l = 0
        return self.reverse_merge_interal(nums, l, r)

    def reverse_merge_interal(self, nums: List[int], s: int, e: int):
        if s == e:
            return[]
        elif e == s+1:
            return [nums[s]]
        else:
            m = int((s + e)/2)
        left = self.reverse_merge_interal(nums, s, m)
        right = self.reverse_merge_interal(nums, m, e)
        return self.mergeAllArray(left, right)
    def mergeAllArray(self, n1: List[int], n2:List[int]):
        result = []
        p1 = 0
        p2 = 0

        while(p1<len(n1) and p2<len(n2)):
            v1 = n1[p1]
            v2 = n2[p2]
            if(v1<v2):
                result.append(v2)
                p2 = p2+1
            else:
                result.append(v1)
                p1 = p1+1
        while(p1<len(n1)):
            result.append(n1[p1])
            p1 = p1+1
        while(p2<len(n2)):
            result.append(n2[p2])
            p2 = p2+1
        return result




example = Solution()
print(example.reverseMerge([]))
print(example.reverseMerge([1]))
print(example.reverseMerge([2, 1]))
print(example.reverseMerge([3, 1, 2]))
print(example.reverseMerge([4, 3, 1, 2]))
print(example.reverseMerge([1, 3, 2, 4, 5])) # => [5, 4, 3, 2, 1]
print(example.reverseMerge([4, 5, 3, 2, 1])) # => [5, 4, 3, 2, 1]
print(example.reverseMerge([3, 1, 5, 2, 6])) # => [6, 5, 3, 2, 1]
print(example.reverseMerge([1, 3, 2, 5])) # => [5, 3, 2, 1]
print(example.reverseMerge([1, 5, 3])) # => [5, 3, 1]
print(example.reverseMerge([1, 3, 4, 3])) # => [4, 3, 3, 1]
