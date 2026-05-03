class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        rev = int(str(n)[::-1])

        start = min(n, rev)
        end = max(n, rev)
        
        def is_prime(x):
            if x <= 1:
                return False
            i = 2
            while i  <= x**0.5:
                if x % i == 0:
                    return False
                i += 1
            return True
        
        total = 0
        for i in range(start, end + 1):
            if is_prime(i):
                total += i

        return total