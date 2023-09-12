class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        m = [1,1]
        for _ in range(n-1):
            tmp = m[1]
            m[1] = m[0] + m[1]
            m[0] = tmp
        return m[1]

    

print(Solution().climbStairs(5))
    # _ _ _ _ 
    # ^