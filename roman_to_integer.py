class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        if s == "":
            return 0

        idx = len(s) - 2
        sum = ROMAN[s[-1]]
        while idx >= 0:
            if ROMAN[s[idx]] >= ROMAN[s[idx + 1]]:
                sum += ROMAN[s[idx]]
            else:
                sum -= ROMAN[s[idx]]
            idx -= 1
        return sum