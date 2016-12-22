class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        pos = 0
        for i in xrange(len(nums)):
            if nums[i] != val:
                nums[pos] = nums[i]
                pos += 1
        return pos


s = Solution()
print s.removeElement([1, 2, 2, 3, 1, 2, 3], 3)
