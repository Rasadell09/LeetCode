class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        trimmed_str = str.lstrip()
        if trimmed_str == '':
            return 0
        else:
            res = []
            for i in xrange(len(trimmed_str)):
                if i == 0 and trimmed_str[i] == '-':
                    res.append(trimmed_str[i])
                elif i == 0 and trimmed_str[i] == '+':
                    continue
                elif trimmed_str[i].isdigit():
                    res.append(trimmed_str[i])
                else:
                    break
            tmps = "".join(res)
            if tmps == '':
                return 0
            elif tmps == '-':
                return 0
            final = int(tmps)
            if final > -pow(2, 31) and final < pow(2, 31) - 1:
                return final
            elif final <= -pow(2, 31):
                return -pow(2, 31)
            elif final >= pow(2, 31) - 1:
                return pow(2, 31) - 1


s = Solution()
print s.myAtoi("   -0012a 42")
