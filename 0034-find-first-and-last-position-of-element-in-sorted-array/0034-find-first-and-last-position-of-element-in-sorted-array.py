class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        def findFirst():
            l, r = 0, n - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    ans = mid
                    r = mid - 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return ans
            
        def findLast():
            l, r = 0, n - 1
            ans = -1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    ans = mid 
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return ans

        return [findFirst(), findLast()]