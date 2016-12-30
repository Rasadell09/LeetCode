class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in xrange(len(s)):
            res +=  pow(26, len(s) - 1 - i) * (ord(s[i]) - 64)
        return res


s = Solution()
print s.titleToNumber('Z')
