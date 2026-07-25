class Solution:
    def maxProduct(self, n: int) -> int:
        res = []
        while n > 0:
            digit = n % 10
            res.append(digit)
            n = n // 10
        res.sort(reverse = True)
        return (res[0] * res[1])