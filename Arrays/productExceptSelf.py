from typing import List


class Solution:
    def productExceptSelf(nums: List[int]) -> List[int]:
        prefix = list(range(len(nums)))
        postfix = list(range(len(nums)))
        output = list(range(len(nums)))
        
        # [1, 2, 3, 4]
        # [1, 2, 6, 24]
        # [24, 24, 12, 4]
        # [1 * 24, 1 * 12, 2 * 4, 6 * 1]

        # [1,2,3,4]
        # [24,12,8,6]
        # 
        # prev = 4 * 3 * 2

        # calculate the prefix of each value in nums
        for index in range(len(nums)):
            if index == 0:
                output[index] = nums[0]
            else:
                output[index] = nums[index] * output[index - 1]
        print(output)
        # calculate the postfix 
        prev = 1
        for index in range(len(nums) - 1, -1, -1):
            temp = nums[index]
            if index - 1 < 0:
                output[index] = prev * 1
            else:
                output[index] = prev * output[index - 1]
            prev *= temp
        print(output)
        return output
    
        # [1, 2, 3, 4]
        # [1, 2, 6, 24]
        # [24, 24, 12, 4]
        # [1 * 24, 1 * 12, 2 * 4, 6 * 1]

        # calculate the prefix of each value in nums
        # for index in range(len(nums)):
        #     if index == 0:
        #         prefix[index] = nums[0]
        #     else:
        #         prefix[index] = nums[index] * prefix[index - 1]

        # # calculate the postfix 
        # for index in range(len(nums) - 1, -1, -1):
        #     if index == len(nums) - 1:
        #         postfix[index] = nums[-1]
        #     else:
        #         postfix[index] = nums[index] * postfix[index + 1]

        # # calculate output
        # for index in range(len(nums)):
        #     if index - 1 < 0:
        #         left = 1
        #     else:
        #         left = nums[index - 1]
        #     if index + 1 > len(nums):
        #         right = 1
        #     else: 
        #         right = nums[index + 1]
        #     output[index] = left * right
        # return output
    
Solution.productExceptSelf(nums=[1,2,3,4])