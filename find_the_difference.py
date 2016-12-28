class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        check = [0 for j in xrange(len(t))]
        for c in s:
            for i in xrange(len(t)):
                if c == t[i] and check[i] == 0:
                    check[i] = 1
                    break
        for k in xrange(len(check)):
            if check[k] == 0:
                return t[k]

        # code = 0
        # for ch in s + t:
        #     code ^= ord(ch)
        # return chr(code)
