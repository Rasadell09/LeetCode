class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1
        while idx < len(nums):
            nums[idx] = 0
            idx += 1
        print nums


s = Solution()
s.moveZeroes([0, 1, 0, 3, 12])
