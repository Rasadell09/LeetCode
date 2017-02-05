class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for e in findNums:
            t = nums.index(e)
            f = True
            for i in xrange(t, len(nums)):
                if nums[i] > e:
                    res.append(nums[i])
                    f = False
                    break
            if f:
                res.append(-1)
        return res


s = Solution()
print s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
