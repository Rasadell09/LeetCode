class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) != 9:
            return False

        for r in board:
            if len(r) != 9:
                return False

        for r in board:
            check_list = [0 for i in xrange(10)]
            for c in r:
                if c == '.':
                    continue
                if c < '0' or c > '9':
                    return False
                if c.isdigit():
                    t = int(c)
                    if check_list[t] != 0:
                        return False
                    else:
                        check_list[t] += 1
                else:
                    return False

        for i in xrange(len(board[0])):
            check_list = [0 for k in xrange(10)]
            for j in xrange(len(board)):
                if board[j][i] == '.':
                    continue
                if board[j][i] < '0' or board[j][i] > '9':
                    return False
                if board[j][i].isdigit():
                    t = int(board[j][i])
                    if check_list[t] != 0:
                        return False
                    else:
                        check_list[t] += 1
                else:
                    return False

        for i in xrange(9):
            r = i / 3
            c = i % 3
            check_list = [0 for x in xrange(10)]
            print r, ' ', c, ' ', check_list
            for j in xrange(3):
                sr = r * 3 + j
                for k in xrange(3):
                    sc = c * 3 + k
                    print sr, ' ', sc
                    if board[sr][sc] == '.':
                        continue
                    if board[sr][sc] < '0' or board[sr][sc] > '9':
                        return False
                    if board[sr][sc].isdigit():
                        t = int(board[sr][sc])
                        if check_list[t] != 0:
                            return False
                        else:
                            check_list[t] += 1
                    else:
                        return False

        return True


s = Solution()
print s.isValidSudoku([['5', '3', '.', '.', '7', '.', '.', '.', '.'],
                       ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
                       ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
                       ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
                       ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
                       ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
                       ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
                       ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                       ['.', '.', '.', '.', '8', '.', '.', '7', '9']])
