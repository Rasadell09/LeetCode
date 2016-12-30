class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check = set(nums)
        for i in check:
            cnt = nums.count(i)
            if cnt > math.floor(len(nums) / 2):
                return i