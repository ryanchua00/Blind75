from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def isSubstring(s:str, t:str):
            return s[:len(t)] == t
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s), -1, -1):
            for word in wordDict:
                print(s[i:])
                if isSubstring(s[i:], word):
                    print(i, word, dp)
                    dp[i] = dp[i + len(word)]
                    if dp[i]: 
                        break
        print(dp)
        return dp[0]

Solution().wordBreak(s = "abcd", wordDict = ["a","abc","b","cd"])


 
#       catsandog -cats-> andog
#                 -cat-> sandog -sand-> og
#   
# 
# 
# 
# 
# 
# 
# 
# 
