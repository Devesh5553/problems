class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perms = []
        count ={ n: 0 for n in nums}
        for num in nums:
            count[num] += 1
        def dfs():
            if len(nums) == len(perms):
                res.append(perms.copy())
                return
            for num in count:
                if count[num] > 0:
                    perms.append(num)
                    count[num] -= 1
                    dfs()
                    count[num] += 1
                    perms.pop()
        dfs()
        return res