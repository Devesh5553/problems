class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        curr = s[0]
        for i in range(1, len(s)):
            value = abs(int(curr) - int(s[i]))
            if value > 2:
                return False
            curr = s[i]
        return True