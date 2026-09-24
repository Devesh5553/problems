class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            tot = 0
            while nums[i] > 0:
                digit = nums[i] % 10
                tot += digit
                nums[i] = nums[i] // 10
            print(tot)
            if tot == i:
                return i
        return -1