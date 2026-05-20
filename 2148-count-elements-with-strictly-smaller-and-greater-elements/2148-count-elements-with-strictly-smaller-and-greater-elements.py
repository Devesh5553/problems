class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_ele = max(nums)
        min_ele = min(nums)
        res = len(nums) - nums.count(max_ele) - nums.count(min_ele)
        return 0 if len(nums) == nums.count(max_ele) else res