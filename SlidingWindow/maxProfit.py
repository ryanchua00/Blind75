from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumProfit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                maximumProfit = max(maximumProfit,prices[right] - prices[left])
            else: 
                left = right
            right += 1
        return maximumProfit
    
print(Solution().maxProfit([1,2]))