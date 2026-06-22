class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = [0] * 26
        for c in text:
            freq[ord(c) - ord("a")] += 1
        bcount = freq[1] // 1 
        acount = freq[0] // 1 
        lcount = freq[11] // 2 
        ocount = freq[14] // 2 
        ncount = freq[13] // 1
        return min(bcount, acount, lcount, ocount, ncount)