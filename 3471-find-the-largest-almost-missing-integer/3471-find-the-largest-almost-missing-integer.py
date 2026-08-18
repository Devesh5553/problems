class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        n = len(nums)
        res = -1
        l, r = 0, k - 1
        if k == n:
            return max(nums)
        while r < n:
            for i in range(l, r + 1):
                freq[nums[i]] += 1
            l += 1
            r += 1

        for key, value in freq.items():
            if value == 1:
                res = max(res, key)
        print(freq)
        return res