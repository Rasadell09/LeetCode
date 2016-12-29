class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        check = [0 for i in xrange(26)]
        for c in s:
            check[ord(c) - ord('a')] += 1
        for i in xrange(len(s)):
            if check[ord(s[i]) - ord('a')] == 1:
                return i
        return -1


s = Solution()
print s.firstUniqChar('cc')
