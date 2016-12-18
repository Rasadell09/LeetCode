class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zigzag = [[] for r in xrange(numRows)]
        t = numRows - 1
        if numRows == 1 or numRows >= len(s):
            return s
        for c in xrange(len(s)):
            zigzag[t - abs(t - c % (2 * t))].append(s[c])
        print ''.join([''.join(zigzag[r]) for r in xrange(numRows)])

s = Solution()
s.convert('ABC', 2)
