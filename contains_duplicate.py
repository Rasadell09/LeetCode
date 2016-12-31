class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        check = collections.Couter(nums)
        for x in check:
            if check[x] > 1:
                return True
        return False
        # return len(nums) != len(set(nums)
