class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == '0' and b == '0':
            return '0'
        max_len = max(len(a), len(b))
        plus_list = ['0' for i in xrange(max_len)]
        idx = len(plus_list) - 1
        idx_a = len(a) - 1
        idx_b = len(b) - 1
        final = []
        while idx_a >= 0 or idx_b >= 0:
            if idx_a < 0:
                if b[idx_b] == '0' and plus_list[idx] == '0':
                    final.insert(0, '0')
                elif b[idx_b] == '0' and plus_list[idx] == '1':
                    final.insert(0, '1')
                elif b[idx_b] == '1' and plus_list[idx] == '0':
                    final.insert(0, '1')
                elif b[idx_b] == '1' and plus_list[idx] == '1':
                    final.insert(0, '0')
                    plus_list[idx - 1] = '1'
            elif idx_b < 0:
                if a[idx_a] == '0' and plus_list[idx] == '0':
                    final.insert(0, '0')
                elif a[idx_a] == '0' and plus_list[idx] == '1':
                    final.insert(0, '1')
                elif a[idx_a] == '1' and plus_list[idx] == '0':
                    final.insert(0, '1')
                elif a[idx_a] == '1' and plus_list[idx] == '1':
                    final.insert(0, '0')
                    plus_list[idx - 1] = '1'
            else:
                if a[idx_a] == '0' and b[idx_b] == '0' \
                        and plus_list[idx] == '0':
                    final.insert(0, '0')
                elif a[idx_a] == '0' and b[idx_b] == '0' \
                        and plus_list[idx] == '1':
                    final.insert(0, '1')
                elif a[idx_a] == '1' and b[idx_b] == '0' \
                        and plus_list[idx] == '0':
                    final.insert(0, '1')
                elif a[idx_a] == '1' and b[idx_b] == '0' \
                        and plus_list[idx] == '1':
                    final.insert(0, '0')
                    plus_list[idx - 1] = '1'
                elif a[idx_a] == '0' and b[idx_b] == '1' \
                        and plus_list[idx] == '0':
                    final.insert(0, '1')
                elif a[idx_a] == '0' and b[idx_b] == '1' \
                        and plus_list[idx] == '1':
                    final.insert(0, '0')
                    plus_list[idx - 1] = '1'
                elif a[idx_a] == '1' and b[idx_b] == '1' \
                        and plus_list[idx] == '0':
                    final.insert(0, '0')
                    plus_list[idx - 1] = '1'
                elif a[idx_a] == '1' and b[idx_b] == '1' \
                        and plus_list[idx] == '1':
                    final.insert(0, '1')
                    if idx > 0:
                        plus_list[idx - 1] = '1'
                    else:
                        plus_list.insert(0, '1')
            idx -= 1
            idx_a -= 1
            idx_b -= 1
        if len(plus_list) > max_len:
            final.insert(0, '1')
        if final[0] == '0':
            final.insert(0, '1')
        return ''.join(final)


s = Solution()
print s.addBinary('1111', '1111')
