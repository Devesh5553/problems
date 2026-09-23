class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        tot = sum(nums)
        target = tot - x
        if target == 0:
            return len(nums)
        l = 0
        curr = 0
        res = 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr > target and r >= l:
                curr -= nums[l]
                l += 1
            if curr == target:
                res = max(res, r - l + 1)
        
        return -1 if res == 0 else len(nums) - res