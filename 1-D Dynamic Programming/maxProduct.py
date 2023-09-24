from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # A subarray of input
        # return largest product
        res = nums[0]
        rMax, rMin = res, res
        for i in range(1, len(nums)):
            if nums[i] < 0:
                temp = rMax
                rMax = rMin
                rMin = temp
            elif nums[i] == 0:
                rMin = 1
                rMax = 1
            rMax = max(rMax * nums[i], nums[i])
            rMin = min(rMin * nums[i], nums[i])
            res = max(res, rMax)
        return res


print(Solution().maxProduct([-2]))


# 
#                 [2,3,-2,4]
#                /  \    \    \  
#              [2]  [3]  [-2]  [4]
#              /        \     \
#            [2,3]    [3,-2]   [-2,4]
#                \         \     
#    X         [2,3,-2]  [3,-2, 4] X
#                    \
#                  [2,3,-2,4] X
# 
