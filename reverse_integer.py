class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        tmp_s = str(x)
        re_s = tmp_s[::-1]
        new_s = []
        if re_s[len(re_s) - 1] == '-':
            new_s = '-' + re_s[:len(re_s) - 1]
        else:
            new_s = re_s
        tmp_res = int(new_s)
        if (tmp_res < (pow(2, 31) - 1)) and (tmp_res > (1 - pow(2, 31))):
            return tmp_res
        else:
            return 0

s = Solution()
print s.reverse(1563847412)
