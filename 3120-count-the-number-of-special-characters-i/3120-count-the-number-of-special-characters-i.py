class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        s = set(word)
        for c in s:
            if c.islower() and c.upper() in word:
                count += 1
        return count