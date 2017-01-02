class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 6:
            print 'n = ', n
            next = 0
            while n:
                next += (n % 10) * (n % 10)
                print next
                n /= 10
            n = next
            print 'n = ', n
        return n == 1


s = Solution()
print s.isHappy(7)
