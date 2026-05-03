class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums)
        for i in range(len(nums)):
            score = 0
            if nums[i] % 2 == 0:
                for j in range(i+1, len(nums)):
                    if nums[j] % 2 == 1:
                        score += 1
                res[i] = score
            if nums[i] % 2 == 1:
                for j in range(i+1, len(nums)):
                    if nums[j] % 2 == 0:
                        score += 1
                res[i] = score
        return res
            
                
                    