class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        res = 1
        for k in range(1, n):
            tot = (k*(k+1)) / 2 
            if tot <= n:
                res = max(res, k)
        return res