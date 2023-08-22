from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        print(sorted([9,1,4,7,3,-1,0,5,8,-1,6]))
        for num in nums:
            length = 1
            if (num - 1) not in numSet:
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    

Solution().longestConsecutive([1])