class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def solve(c):
            freq = defaultdict(int)
            for i in range(len(c)):
                freq[c[i]] += 1
            for i in range(len(c)):
                if freq[c[i]] < k:
                    return max(solve(part) for part in c.split(c[i]))
            return len(c)
        return solve(s)