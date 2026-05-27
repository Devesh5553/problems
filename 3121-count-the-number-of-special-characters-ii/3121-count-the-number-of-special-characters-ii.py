class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = {}
        upper = {}
        count = 0
        for i in range(len(word)):
            if word[i].islower():
                lower[word[i]] = i
            else:
                if word[i] not in upper:
                    upper[word[i]] = i
        for key in lower:
            if key.islower():
                if key.upper() in upper and upper[key.upper()] > lower[key]:
                    count += 1    
        return count