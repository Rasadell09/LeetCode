class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if matrix == []:
            return []
        else:
            if len(matrix) == 1:
                return matrix[0]
            elif len(matrix) > 1 and len(matrix[0]) == 1:
                for r in matrix:
                    for e in r:
                        res.append(e)
                return res
            else:
                res.append(matrix[0][0])
                res.append(matrix[0][1])
                res.append(matrix[1][0])
                M = len(matrix)
                N = len(matrix[0])
                leng = M * N - 3
                lastx = 1
                lasty = 0
                f = False
                while leng > 0:
                    if f:
                        if lastx - 1 < 0 or lasty + 1 >= N:
                            f = False
                            if lastx - 1 < 0 and lasty + 1 < N:
                                lastx = 0
                                lasty += 1
                                res.append(matrix[lastx][lasty])
                            elif lastx - 1 >= 0 and lasty + 1 >= N:
                                lastx += 1
                                lasty = N - 1
                                res.append(matrix[lastx][lasty])
                            else:
                                lastx += 1
                                lasty = N - 1
                                res.append(matrix[lastx][lasty])
                        else:
                            lastx -= 1
                            lasty += 1
                            res.append(matrix[lastx][lasty])
                    else:
                        if lastx + 1 >= M or lasty - 1 < 0:
                            f = True
                            if lastx + 1 >= M and lasty - 1 >= 0:
                                lastx = M - 1
                                lasty += 1
                                res.append(matrix[lastx][lasty])
                            elif lastx + 1 < M and lasty - 1 < 0:
                                lastx += 1
                                lasty = 0
                                res.append(matrix[lastx][lasty])
                            else:
                                lastx = M - 1
                                lasty += 1
                                res.append(matrix[lastx][lasty])
                        else:
                            lastx += 1
                            lasty -= 1
                            res.append(matrix[lastx][lasty])
                    leng -= 1
                return res


s = Solution()
print s.findDiagonalOrder([[2,5],[8,4],[0,-1]])

