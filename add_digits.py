import math
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return int(num - 9 * math.floor((n - 1) / 9))