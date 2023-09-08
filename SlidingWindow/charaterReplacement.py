class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 1
        charCount = {}
        charCount[s[0]] = 1
        maxCount = 0
        while end < len(s):
            longestChar = max(charCount.values())
            print(charCount)
            print("longestChar + k:", longestChar+k, "end-start:", end-start)
            charCount[s[end]] = charCount.get(s[end], 0) + 1
            if longestChar + k >= end - start:
                maxCount = max(maxCount, min(len(s), max(longestChar, max(charCount.values())) + k))
            else:
                print("Skipping at start:", start, "end:", end)
                while longestChar + k < end - start:
                    charCount[s[start]] -= 1
                    start += 1

            end += 1
        print(charCount)
        return max(maxCount, min(max(charCount.values()) + k, len(s)))
    
print(Solution().characterReplacement("AAAAABBBBCBB", 4))

# s = "AAAAABBBBCBB", k = 4
#       ^        ^

# s ="ABCCCCC", k = 2
#     ^     ^ 

# s = "ABAB", k = 2
#      ^^^^

# s = "AABABBA", k = 1
#          ^^^

# Iterate through while right < len(s)
    # Extend right side of window while max_key_count + k = len(window)
    # keep max
        # If not able to, shift left side until condition is reached. 