class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        if not nums:
            return -1
        min_index, r = 0, n - 1
        while min_index < r:
            m = (min_index + r) // 2
            if nums[m] > nums[r]:
                min_index = m + 1
            else:
                r = m
        max_index = (min_index - 1) % n
        if target >= nums[0]:
            l, r = 0, max_index
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        else:
            l, r = max_index + 1, n -1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1