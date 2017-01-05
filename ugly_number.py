import math


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for e in [2, 3, 5]:
            while num % e == 0:
                num /= e
        return num == 1


s = Solution()
print s.isUgly(90)
