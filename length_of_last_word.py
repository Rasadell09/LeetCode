class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        idx = s.rfind(' ')
        return len(s) - (idx + 1)


s = Solution()
print s.lengthOfLastWord("Hello ")
