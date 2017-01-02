class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        if num < 0:
            num = num + 2**32
        while num != 0:
            t = num % 16
            if t >= 10:
                res.append(chr(t + 87))
            else:
                res.append(str(t))
            num /= 16
        if res == []:
            return '0'
        res.reverse()
        return ''.join(res)


s = Solution()
print s.toHex(0)
