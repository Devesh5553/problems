class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, 101):
            pro = 1
            res = i
            while i > 0:
                digit = i % 10
                i = i // 10
                pro *= digit
            if pro % t == 0:
                return res
                break