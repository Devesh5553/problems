class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        big = max(nums)
        higher = max(small, big)
        boool = True
        while boool:
            if higher % small == 0 and higher % big == 0:
                lcm = higher
                boool = False
            higher += 1
        gcd = abs(small * big) // lcm
        return gcd