class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set for O(1) checking of item
        # count
        # pointer 
        start = 0
        end = 0
        maxCount = 0
        substring = set()
        while end < len(s) :
            if s[end] not in substring:
                substring.add(s[end])
            else:
                maxCount = max(maxCount, len(substring))

                # move the window up to a non-duplicate position
                #  s = "abcaecbb"
                #              ^ 

                while s[end] in substring:
                    substring.remove(s[start])
                    start += 1
                substring.add(s[end])
            end += 1
        return max(maxCount, len(substring))
    
print(Solution().lengthOfLongestSubstring(" "))