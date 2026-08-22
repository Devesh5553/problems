class Solution:
    def checkDivisibility(self, n: int) -> bool:
        tot = 0
        pro = 1
        t = n
        while t > 0:
            digit = t % 10
            tot += digit
            pro *= digit
            t = t // 10
        res = tot + pro
        if n % res == 0:
            return True
        else:
            return False
        