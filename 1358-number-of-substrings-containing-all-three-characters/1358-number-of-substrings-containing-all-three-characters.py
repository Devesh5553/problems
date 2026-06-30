class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a':0, 'b':0, 'c':0}
        l, r = 0, 0
        res = 0
        while r < len(s):
            count[s[r]] += 1
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                res += len(s) - r
                count[s[l]] -= 1
                l += 1
            r += 1
        return res