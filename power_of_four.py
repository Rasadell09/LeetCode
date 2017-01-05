import math


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        return (math.log10(num) / math.log10(4)) % 1 == 0


s = Solution()
print s.isPowerOfFour(56)
