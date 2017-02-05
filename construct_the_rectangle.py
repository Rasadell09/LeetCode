class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """        
        dest = 2**31
        res = [-1 for i in xrange(2)]
        for i in xrange(1, int(math.sqrt(area)) + 1):
            if area % i == 0:
                L = area / i
                if L - i < dest:
                    res[0] = L
                    res[1] = i
        return res