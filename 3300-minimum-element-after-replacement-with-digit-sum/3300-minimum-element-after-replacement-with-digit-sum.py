class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum_num = 0
            for dig in str(nums[i]):
                sum_num += int(dig)
            nums[i] = sum_num
        return min(nums)