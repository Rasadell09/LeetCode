class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_bin = str(bin(x))
        y_bin = str(bin(y))
        x_bin = x_bin[2:]
        y_bin = y_bin[2:]
        if len(x_bin) > len(y_bin):
            for i in xrange(len(x_bin) - len(y_bin)):
                y_bin = '0' + y_bin[0:]
        else:
            for i in xrange(len(y_bin) - len(x_bin)):
                x_bin = '0' + x_bin[0:]
        d = 0
        for i in xrange(len(x_bin)):
            if x_bin[i] != y_bin[i]:
                d += 1
        return d

s = Solution()
print s.hammingDistance(4, 2)