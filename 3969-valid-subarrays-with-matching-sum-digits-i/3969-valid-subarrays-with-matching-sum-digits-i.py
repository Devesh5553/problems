class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        res = 0
        for i in range(len(nums)):
            tot = 0
            for j in range(i, len(nums)):
                tot += nums[j]
                str_tot = str(tot)
                if str_tot[0] == str(x) and str_tot[-1] == str(x):
                    res += 1
        return res