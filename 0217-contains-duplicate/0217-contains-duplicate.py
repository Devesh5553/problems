class Solution(object):
    def containsDuplicate(self, nums):
        iterated = set()
        for value in nums:
            if value in iterated:
                return True
            iterated.add(value)
        return False

        """
        :type nums: List[int]
        :rtype: bool
        """
        