from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        first_ptr = 0
        enumerate(nums)
        while first_ptr <= len(nums) - 3:
            second_ptr = first_ptr + 1
            third_ptr = len(nums) - 1
            if first_ptr > 0 and nums[first_ptr - 1] == nums[first_ptr]:
                pass
            else:
                while second_ptr < third_ptr:

                    sum = nums[first_ptr] + nums[second_ptr] + nums[third_ptr]
                    if sum < 0:
                        second_ptr += 1
                    elif sum > 0:
                        third_ptr -= 1
                    else:
                        res.append([nums[first_ptr], nums[second_ptr], nums[third_ptr]])              
                        second_ptr += 1
                        while nums[second_ptr] == nums[second_ptr - 1] and second_ptr < third_ptr:
                            second_ptr += 1
            first_ptr += 1
        return res
    
print(Solution().threeSum([-1,0,1,2,-1,-4,0,0,0,0,0]))