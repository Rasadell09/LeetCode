class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPri = 2**32
        maxPro = 0
        for x in prices:
            minPri = min(minPri, x)
            maxPro = max(maxPro, x - minPri)
        return maxPro


s = Solution()
print s.maxProfit([7, 1, 5, 3, 3, 6, 4])
