from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit = 0
        for num in nums:
            bit = bit ^ num
        return bit
    
# 00000000 00000000 00000000 00000010