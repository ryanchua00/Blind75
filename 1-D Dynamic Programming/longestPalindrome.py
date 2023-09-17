class Solution:
    # Memoize
    def pretty_print(self, s: any):
        for row in s:
            for col in row:
                if col == True:
                    print(str(col) + "  ", end="")
                else:
                    print(str(col) + " ", end="")
            print()

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        longest_palindrome_start, longest_palindrome_len = 0, 1

        for end in range(0, n):
            for start in range(end - 1, -1, -1):
                self.pretty_print(dp)
                print('start: %s, end: %s, s: %s' % (start, end, s[start:end]))
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        palindrome_len = end - start + 1
                        if longest_palindrome_len < palindrome_len:
                            longest_palindrome_start = start
                            longest_palindrome_len = palindrome_len
        print(longest_palindrome_len, longest_palindrome_start)
        return s[longest_palindrome_start: longest_palindrome_start + longest_palindrome_len]
        # include current word in current palindrome
        # dont include current word in current palindrome
    #     if s in self.res: return self.res[s]
    #     # print(s, s[0:len(s)-1], s[1:len(s)])
    #     print(self.res)
    #     if len(s) <= 1: return s
    #     if self.isPalindrome(s): 
    #         self.res[s] = s
    #         return s
        
    #     # Convert this iteratively
    #     left = self.longestPalindrome(s[0:len(s)-1])
    #     right = self.longestPalindrome(s[1:len(s)])

    #     if len(left) > len(right):
    #         self.res[left] = left
    #         return left
    #     else:
    #         self.res[right] = right
    #         return right

    # def isPalindrome(self, s:str) -> bool:
    #     p0, p1 = 0, len(s) - 1
    #     while p0 < p1:
    #         if s[p0] != s[p1]: return False
    #         p0 += 1
    #         p1 -= 1
    #     return True
    
print(Solution().longestPalindrome("babad"))
# "babadd" babad abadd
# babad baba abad
# baba bab aba

# "bab"
#    >b      a      >b
# [>[true, false, false],
#  [false, true ,false],
#  [false, false, true]]