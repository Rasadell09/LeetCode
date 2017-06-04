class Solution(object):
    def countBits(self, num):
        res = []
        res[0] = 0
        res[1] = 1
        tail = []
        tail[0] = 0
        tail[1] = 1
        