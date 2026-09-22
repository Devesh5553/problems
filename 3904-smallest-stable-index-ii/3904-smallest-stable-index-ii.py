class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        preMax = [0] * len(nums)
        preMax[0] = nums[0]
        for i in range(1, len(nums)):
            preMax[i] = max(preMax[i - 1], nums[i])

        suffMin = [0] * len(nums)
        suffMin[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffMin[i] = min(suffMin[i + 1], nums[i])

        for i in range(len(nums)):
            if preMax[i] - suffMin[i] <= k:
                return i
        return -1