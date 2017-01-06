class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
            print i, last, now
        return now


s = Solution()
print s.rob([30, 1, 1, 0, 2, 10])
