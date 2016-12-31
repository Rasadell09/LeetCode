class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        check_upper = [0 for i in xrange(26)]
        check_lower = [0 for i in xrange(26)]
        for c in s:
            if ord(c) >= 65 and ord(c) <= 90:
                check_upper[ord(c) - 65] += 1
            if ord(c) >= 97 and ord(c) <= 122:
                check_lower[ord(c) - 97] += 1
        res = 0
        f = False
        for x in xrange(len(check_lower)):
            if check_lower[x] % 2 != 0:
                res += check_lower[x] - 1
                f = True
            if check_upper[x] % 2 != 0:
                res += check_upper[x] - 1
                f = True
            if check_lower[x] % 2 == 0 and check_lower[x] != 0:
                res += check_lower[x]
            if check_upper[x] % 2 == 0 and check_upper[x] != 0:
                res += check_upper[x]
        if f:
            res += 1
        return res


s = Solution()
print s.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")
