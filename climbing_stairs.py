class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = [0 for k in xrange(n + 1)]
        for i in xrange(n + 1):
            if i <= 1:
                s[i] = 1
            else:
                s[i] = s[i - 1] + s[i - 2]
        return s[n]


s = Solution()
print s.climbStairs(35)