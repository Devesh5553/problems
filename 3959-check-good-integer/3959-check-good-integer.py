class Solution(object):
    def checkGoodInteger(self, n):
        digitSum, squareSum = 0, 0
        num = n
        if len(str(num)) == 1:
            square = num**2
            return True if square - num >= 50 else False
        while len(str(num)) > 1:
            digit = num % 10
            digitSum += digit
            squareSum += digit**2
            num = num // 10
        digitSum += num
        squareSum += num ** 2
        res = squareSum - digitSum
        if res >= 50:
            return True
        else:
            return False