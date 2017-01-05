class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        ll = s.split(' ')
        for e in ll:
            if e != '':
                cnt += 1
        return cnt


s = Solution()
print s.countSegments('  Hello, al asdf e fwe   fw wef  ')
