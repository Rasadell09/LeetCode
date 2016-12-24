class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        idx = len(digits) - 1
        plus_one_list = [0 for i in xrange(len(digits) - 1)]
        plus_one_list.append(1)
        if idx == -1:
            return [1]
        else:
            while idx >= 0:
                digits[idx] += plus_one_list[idx]
                if digits[idx] > 9:
                    digits[idx] = 0
                    plus_one_list[idx - 1] = 1
                idx -= 1
            if digits[0] == 0:
                digits.insert(0, 1)
        return digits


s = Solution()
print s.plusOne([9, 9])
