class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
            
        tail = 0
        for i in xrange(len(nums)):
            if nums[i] != nums[tail]:
                tail += 1
                nums[tail] = nums[i]
        return tail + 1


s = Solution()
print s.removeDuplicates([1, 1, 1, 2, 3, 3, 4])
