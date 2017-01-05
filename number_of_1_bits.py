class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n != 0:
            if n & 1:
                res += 1
            n >>= 1
        return res


s = Solution()
print s.hammingWeight(126)
