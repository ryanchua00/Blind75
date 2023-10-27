class Solution:
    def firstUniqChar(self, s: str) -> int:
        charMap = {}
        seen = set()
        for i in range(len(s)):
            if s[i] not in charMap:
                charMap[s[i]] = i 
            else:
                seen.add(s[i])
                charMap.pop(s[i])

        for item in seen:
            if item in iter(charMap.keys()):
                charMap.pop(item)

        if len(charMap)> 0:
            return next(iter(charMap.values()))
        else:
            return -1
        
print(Solution().firstUniqChar("loveleetcode"))