class Solution:
    def maxDepth(self, s: str) -> int:
        cur, res = 0, 0
        for c in s:
            if c == "(":
                cur += 1
            elif c == ")":
                cur -= 1
            else:
                continue
            res = max(res, cur)
        return res