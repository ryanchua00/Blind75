class Solution:
    def numDecodings(self, s: str) -> int:
        # valid digits range from 1 -> 26
        # 0 is not valid
        # s is a string of digits
        # output: the number of ways to map s to characters
        dp =  { len(s): 1 }

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else: 
                dp[i] = dp[i+1]
            if (i < len(s) - 1) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp(i+2)
        return dp[0]

        # dp = { len(s): 1 }

        # def dfs(i):
        #     if i in dp:
        #         return dp[i] # base case to count last char in s 
        #     if s[i] == "0":
        #         return 0
            
        #     res = dfs(i+1)
        #     if (i < len(s) - 1) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
        #         res += dfs(i+2)
        #     dp[i] = res
        #     return res
        # ans = dfs(0)
        # print(dp)
        # return ans
    
#               226
#                /\
#               2  26
#              /\   \
#             2 26   2
#            / 
#           6
#
#         p0 = 0
#         count = 0
#         while p0 < len(s):
#             if p0 < len(s) - 1:
#                 # case 2
#                 count += self.numDecodings(s[2:])
#                 # print(count, "after first if")
#             if p0 < len(s) - 1 and s[p0+1] != "0":
#                 # case 1
#                 count += self.numDecodings(s[1:])
#                 # print(count, "after second if")
#             if p0 == len(s) - 1:
#                 # edge case 1
#                 count += 1
#                 # print(count, "after edge case")
#             p0 += 1
#         # case 1: 2 digits char + rest
#         # case 2: 1 digit char + rest 
#         print(count, s)
#         return count

print(Solution().numDecodings("226"))
    # "226"
    # 2 2 6
    # 22 6
    # 2 26
    
    
    # "101"
    #  ^ # can only be 10
    # "0"
    #  ^ dead
    # check the next digit 