class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:

        rev = nums[::-1]
        print(rev)
        for i in rev:
            nums.append(i)
        return nums