from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetDict = {}
        for numsIndex in range(len(nums)):
            if nums[numsIndex] in targetDict:
                return [targetDict[nums[numsIndex]], numsIndex]
            else:
                targetDict[target - nums[numsIndex]] = numsIndex
        
        # assume 1 solution
        # for pair1 in range(len(nums)):
        #     for pair2 in range(pair1 + 1, len(nums)):
        #         if nums[pair1] + nums[pair2] == target:
        #             return [pair1, pair2]