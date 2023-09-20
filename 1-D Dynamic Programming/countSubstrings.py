class Solution:
    def countSubstrings(self, s: str) -> int:
        # if edge chars are the same and centre is a palindrome, it is a palindorme
        substringLength = 1
        count = 0
        setOfPalindromes = set()
        while substringLength - 1 < len(s):
            p0 = 0
            while p0 + substringLength - 1 < len(s):
                substring = s[p0:p0+substringLength]
                if (len(substring) == 1) \
                    or (len(substring) == 2 and substring[0] == substring[-1]) \
                    or (len(substring) > 2 and substring[0] == substring[-1] and substring[1:-1] in setOfPalindromes):
                    count += 1
                    setOfPalindromes.add(substring)
                p0 += 1
            substringLength += 1
        return count
    
print(Solution().countSubstrings("aaa"))