from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob current house and skip prev, but get all after that 
        # skip current, get all after
        if len(nums) == 0: return 0
        prev1 = 0 # represents the prev house 
        prev2 = 0 # represents prev 2 houses 
        for num in nums:
            print(prev1, prev2) 
            tmp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = tmp
        return prev1
    
# [4,4]
#  
#  [1,2,3,1]
#       ^


# print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,7,9,3,1]))
# print(Solution().rob([2,1,1,2]))
# missCost D = C,E   
# A = [A, B, C, D, E]
#      ^  X 
# largest sum of non-adjacent numbesrs

# XYXXXXXX
# YXXXXXXX 
#  XYXXXXX
#  YXXXXXX