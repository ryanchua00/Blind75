from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob current house and skip prev, but get all after that 
        # skip current, get all after
        if len(nums) == 0: return 0
        mem = [0,0]
        for num in nums:
            tmp = mem[0]
            mem[0] = max(mem[1] + num, mem[0])
            mem[1] = tmp
        return mem[0]
    
# [4,4]
#  
#  [1,2,3,1]
#       ^


print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,7,9,3,1]))
print(Solution().rob([2,1,1,2]))
# missCost D = C,E   
# A = [A, B, C, D, E]
#      ^  X 
# largest sum of non-adjacent numbesrs

# XYXXXXXX
# YXXXXXXX 
#  XYXXXXX
#  YXXXXXX