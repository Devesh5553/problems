class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        n = len(nums)
        for i in range(n):
            l, r = i + 1, n - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                tot = nums[i] + nums[l] + nums[r]
                if abs(tot - target) < abs(res - target):
                    res = tot
                if tot > target:
                    r -= 1
                elif tot < target:
                    l += 1
                else:
                    return target
                print(res)
        return res
