from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost: return 0
        dp = [0] * len(cost)
        dp[0] = cost[0]
        if len(cost) >= 2:
            dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        print(dp)
        return min(dp[-1], dp[-2])
    

print(Solution().minCostClimbingStairs([10, 15, 20]))



        # take best path from top - greedy solution
        # curr = len(cost)
        # climbingCost = 0
        # while curr > 1:
        #     if cost[curr - 2] <= cost[curr - 1]:
        #         climbingCost += cost[curr - 2]
        #         curr -= 2
        #     else:
        #         climbingCost += cost[curr - 1]
        #         curr -= 1
        # return climbingCost
    
# cost = [10, 15, 20]
#                      ^
# 
# cost = [1,100,1,1,1,100,1,1,100,1]
#         ^     ^   ^     ^       ^   
#        [1,100,1,1,1,100,1,]
#
#        [1,100,1,1,1,100]     