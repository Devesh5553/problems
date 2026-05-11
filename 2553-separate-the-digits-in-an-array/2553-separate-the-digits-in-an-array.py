class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            str_i= str(i)
            for j in range(len(str_i)):
                res.append(int(str_i[j]))
        return res
