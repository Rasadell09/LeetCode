class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_len = len(s)
        if str_len % 2 == 0:
            half = str_len / 2
        else:
            half = (str_len - 1) / 2

        new_str = list(s)
        for i in xrange(half):
            tmp = new_str[i]
            new_str[i] = new_str[str_len - i - 1]
            new_str[str_len - i - 1] = tmp
        return ''.join(new_str)


s = Solution()
print s.reverseString("hello")
