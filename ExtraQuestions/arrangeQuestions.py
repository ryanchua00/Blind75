class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Build a coin pyramid from top down, left to right
        # input: number of coins
        # output: number of full rows

        # continuously build rows using a loop and a counter
        # if counter > number of coins remaining, return counter - 1
        # if counter <= num coins, subtract frm num coins,
        # increment counter

        row = 1
        numCoins = n
        while True:
            if row > numCoins:
                return row - 1
            else:
                numCoins -= row
            row += 1
        return

# n = 3
# @
# @@ = 2

# n = 7
# @
# @@
# @@@
# @   = 3
