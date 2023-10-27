from typing import List
from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda s : s * -1, stones))
        heapify(stones)
        print(stones)
        while len(stones) > 1:
            y = heappop(stones) * -1
            x = heappop(stones) * -1
            y -= x
            if y > 0: heappush(stones, y * -1)

        if len(stones) > 0:
            return stones[0] * -1
        else:
            return 0
    
    # input: a list of stones.
    #  we smash the heaviest stones, x, y , where x <= y
    #  if x==y  both stones are destroyed
    #  if x != y, x destroyed, y = y-x

stones = [2,7,4,1,8,1]
print(Solution().lastStoneWeight(stones))
stones = [2,2]
print(Solution().lastStoneWeight(stones))
