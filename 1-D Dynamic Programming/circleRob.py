from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # direction doesnt matter since both directions should yield same result
        # if first house chosen, last house can not be selected.
        # sub problems stay the same
        numsFirst = nums.copy()
        numsFirst.pop()
        numsLast = nums.copy()
        numsLast.pop(0)
        return max(self.robHelper(numsFirst), self.robHelper(numsLast))
    
    def robHelper(self, nums: List[int]) -> int:
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


# [1, 2, 3, 4]
#  X  Y  X  Y

# [1, 2, 3, 1, 1]
#              ^  
#
# prev1 = 4
# prev2 = 4

# []