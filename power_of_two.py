import math


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return (math.log10(n) / math.log10(2)) % 1 == 0


s = Solution()
print s.isPowerOfTwo(8)
