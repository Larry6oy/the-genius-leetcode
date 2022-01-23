from typing import DefaultDict, List


class Solution:
    def containsDuplicate_2(self, nums: List[int]) -> bool:
        length = len(nums)
        for c in range(0, length):
            v = nums[c] 
            for c2 in range(c+1, length):
                v2 = nums[c2]
                if v == v2:
                    return True
        return False
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for num in nums:
            if dict.get(num) != None:
                return True
            else:
                dict[num] = True
        return False


example = Solution()

print(example.containsDuplicate([0,1,2,3,4,5,6,7,8,9,10]))