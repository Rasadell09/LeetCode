class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i1 = len(num1) - 1
        i2 = len(num2) - 1
        carry = 0
        res = []
        while i1 >= 0 or i2 >= 0 or carry >= 0:
            sum = 0
            if i1 < 0 and i2 < 0 and carry == 0:
                break
            if i1 >= 0:
                sum += ord(num1[i1]) - ord('0')
                i1 -= 1
            if i2 >= 0:
                sum += ord(num2[i2]) - ord('0')
                i2 -= 1
            sum += carry
            carry = sum / 10
            res.append(str(sum % 10))
        res.reverse()
        return ''.join(res)


s = Solution()
print s.addStrings("0", "0")
