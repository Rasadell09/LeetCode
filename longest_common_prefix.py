class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        idx = 0
        min_len_str = strs[idx]
        for i in xrange(len(strs)):
            if len(strs[i]) < min_len_str:
                min_len_str = len(strs[i])
                idx = i
        short_str = strs[idx]
        chars_list = [0 for i in xrange(min_len_str)]
        for i in xrange(min_len_str):
            for j in xrange(len(strs)):
                if short_str[i] == strs[j][i]:
                    chars_list[i] += 1

        final_res = []
        for i in xrange(min_len_str):
            if chars_list[i] == len(strs):
                final_res.append(short_str[i])
            else:
                break

        return "".join(final_res)


strs = [
        "aba",
        "cba"
        ]
s = Solution()
print s.longestCommonPrefix(strs)