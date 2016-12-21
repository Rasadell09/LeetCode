class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in d.values():
                stack.append(c)
            elif c in d.keys():
                if len(stack) == 0 or d[c] != stack.pop():
                    return False
            else:
                return False

        return len(stack) == 0