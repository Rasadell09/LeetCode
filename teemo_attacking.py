class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        if len(timeSeries) == 0:
            return 0
        for i in xrange(len(timeSeries) - 1):
            if timeSeries[i + 1] - timeSeries[i] > duration:
                res += duration
            else:
                res += timeSeries[i + 1] - timeSeries[i]
        res += duration
        return res