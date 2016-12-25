class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        final = []
        for i in xrange(n):
            if i == 0:
                final.append(str(1))
                continue
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                final.append("FizzBuzz")
            elif (i + 1) % 3 == 0 and (i + 1) % 5 != 0:
                final.append("Fizz")
            elif (i + 1) % 3 != 0 and (i + 1) % 5 == 0:
                final.append("Buzz")
            else:
                final.append(str(i + 1))
        return final


s = Solution()
print s.fizzBuzz(15)
