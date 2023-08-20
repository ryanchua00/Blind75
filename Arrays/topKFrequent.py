from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countOfNums = {}
        for num in nums: 
            count = countOfNums.get(num, 0)
            countOfNums[num] = count + 1    
        sortedCount = dict(sorted(countOfNums.items(), key=lambda item: item[1], reverse=True))
        mostFrequent = list(sortedCount.keys())[:k]
        return mostFrequent