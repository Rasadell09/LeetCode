class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        t = []
        for e in nums:
            t.append(e)
        t.sort()
        t.reverse()
        res = []
        for e in nums:
            if t.index(e) >= 3:
                res.append(str(t.index(e) + 1))
            elif t.index(e) == 2:
                res.append("Bronze Medal")
            elif t.index(e) == 1:
                res.append("Silver Medal")
            elif t.index(e) == 0:
                res.append("Gold Medal")
        return res


s = Solution()
print s.findRelativeRanks([3, 6, 89, 23, 123, 45, 112, 54, 1, 2, 0])
