class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()

        m = (len(nums)) // 2
        arr1 = nums[:m]
        arr2 = nums[m: len(nums)] 

        print(arr1, arr2)
        sum_arr1 = sum(arr1)
        sum_arr2 = sum(arr2)

        return sum_arr2 - sum_arr1           
