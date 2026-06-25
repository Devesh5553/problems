class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        res = 0
        for l in range(len(nums)):
            count_target = 0
            for r in range(l, len(nums)):
                if nums[r] == target:
                    count_target += 1
                length = r - l + 1
                if count_target > length // 2:
                    res += 1
        return res