class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for c in patterns:
            if c in word:
                res += 1
        return res