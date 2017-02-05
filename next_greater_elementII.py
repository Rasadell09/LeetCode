class Solution(object):
    def nextGreaterElement(self, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in xrange(len(nums)):
            f = True
            for j in xrange(i + 1, i + len(nums) - 1):
                if nums[j % len(nums)] > nums[i]:
                    res.append(nums[j % len(nums)])
                    f = False
                    break
            if f:
                res.append(-1)
        return res


s = Solution()
print s.nextGreaterElement([100, 1, 11, 1, 120, 111, 123, 1, -1, -100])
