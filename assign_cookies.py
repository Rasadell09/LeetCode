class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        result = 0
        gidx = 0
        sidx = 0
        while sidx < len(s):
            if s[sidx] >= g[gidx]:
                result += 1
                sidx += 1
                gidx += 1
                if gidx >= len(g):
                    break
            else:
                sidx += 1
        return result


s = Solution()
print s.findContentChildren([1, 2], [1, 2, 3])
