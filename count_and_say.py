class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def next_str(x):
            s = str(x)
            final = []
            num_c = 0
            last_c = s[0]
            for i in xrange(len(s)):
                if s[i] == last_c:
                    num_c += 1
                else:
                    final.append(str(num_c))
                    final.append(last_c)
                    num_c = 1
                last_c = s[i]
            final.append(str(num_c))
            final.append(str(last_c))
            return ''.join(final)
        x = '1'
        for i in xrange(n - 1):
            x = next_str(x)

        return x


s = Solution()
print s.countAndSay(18)
