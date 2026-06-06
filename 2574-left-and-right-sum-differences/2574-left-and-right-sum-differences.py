class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res = []
        leftSum = 0
        sumNums = sum(nums)
        for i in range(len(nums)):
            rightSum = sumNums - leftSum - nums[i]
            res.append(abs(leftSum - rightSum))
            leftSum += nums[i]
        return res