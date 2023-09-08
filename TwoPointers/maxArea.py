from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1, p2 = 0, len(height) - 1
        maxArea = 0
        while p1 < p2:
            area = min(height[p1],height[p2]) * (p2-p1)
            maxArea = max(maxArea, area)
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 += 1

        return maxArea

#     def calculateArea(self, p1, p2, height):
#             waterHeight = min(height[p1], height[p2])
#             waterWidth = p2 - p1 
#             return waterHeight * waterWidth
    
#     def maxArea(self, height: List[int]) -> int:
#         # height will be min(height[p1], height[p2])
#         # width will be p2 - p1
#         largestArea = 0
#         left = 0
#         right = 0
#         p1 = 0
#         p2 = 1

#         # naively calculate all the heights and store largest one
#         while p2 < len(height):
#             print(p1,p2)
#             newArea = self.calculateArea(p1,p2,height)
#             largestArea = max(newArea, largestArea)
                


#             # Move left pointer and search for highest and furthest back
#             p0 = p1
#             while p0 < p2:
#                 print("p0:",p0,"p2:",p2)
#                 newerArea = self.calculateArea(p0,p2,height)
#                 newlargestArea = newArea
#                 if newerArea > newlargestArea:
#                     newlargestArea = newerArea
#                     p1 = p0
#                     break
#                 else:
#                     p0 += 1
#             largestArea = max(newlargestArea, largestArea)
#             # Move right pointer along
#             p2 += 1

#             # if (p2 == len(height)):
#             #     p1 += 1
#             #     p2 = p1 + 1

#         return largestArea
    
# print("maxArea:", Solution().maxArea([1,2,4,3]))
            

#             # [1, 2, 4, 3]
#             #  ^        ^
#             #
#             # largestArea = 3