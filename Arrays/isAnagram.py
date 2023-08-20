class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterCount = {}
        for char in s:
            if char in letterCount:
                letterCount[char] += 1
            else:
                letterCount[char] = 1
        for char in t:
            if char in letterCount:
                letterCount[char] -= 1
            else:
                return False
        for char in letterCount:
            if letterCount[char] > 0:
                return False
        return True