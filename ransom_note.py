class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        check = [97 + i for i in xrange(26)]
        r = 0
        m = 0
        result = True
        for i in xrange(len(check)):
            r = ransomNote.count(chr(check[i]))
            m = magazine.count(chr(check[i]))
            if r > m:
                result = False
                break
        return result


s = Solution()
print s.canConstruct('abacabac', 'aabbbbcccc')
