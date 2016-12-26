class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == 1:
                    if (i == 0 and j == 0) or \
                            (i == 0 and j == len(grid[i]) - 1) or \
                            (i == len(grid) - 1 and j == 0) or \
                            (i == len(grid) - 1 and j == len(grid[i]) - 1):
                        perimeter += 2
                        if i == 0 and j == 0:
                            if grid[i + 1][j] == 1 and grid[i][j + 1] != 1:
                                perimeter += 1
                            elif grid[i + 1][j] != 1 and grid[i][j + 1] == 1:
                                perimeter += 1
                            elif grid[i + 1][j] == 1 and grid[i][j + 1] == 1:
                                perimeter += 2
                            else:
                                continue
                        elif i == 0 and j == len(grid[i]) - 1:
                            if grid[i + 1][j] == 1 and grid[i][j - 1] != 1:
                                perimeter += 1
                            elif grid[i + 1][j] != 1 and grid[i][j - 1] == 1:
                                perimeter += 1
                            elif grid[i + 1][j] == 1 and grid[i][j - 1] == 1:
                                perimeter += 2
                            else:
                                continue
                        elif i == len(grid) - 1 and j == 0:
                            if grid[i][j + 1] == 1 and grid[i - 1][j] != 1:
                                perimeter += 1
                            elif grid[i][j + 1] != 1 and grid[i - 1][j] == 1:
                                perimeter += 1
                            elif grid[i][j + 1] == 1 and grid[i - 1][j] == 1:
                                perimeter += 2
                            else:
                                continue
                        elif i == len(grid) - 1 and j == len(grid[i]) - 1:
                            if grid[i - 1][j] == 1 and grid[i][j - 1] != 1:
                                perimeter += 1
                            elif grid[i - 1][j] == 1 and grid[i][j - 1] != 1:
                                perimeter += 1
                            elif grid[i - 1][j] == 1 and grid[i][j - 1] == 1:
                                perimeter += 2
                            else:
                                continue
                    elif i == 0 or j == 0 or \
                            i == len(grid) - 1 or j == len(grid[i]) - 1:
                        perimeter += 1
                        if i == 0:
                            if grid[i + 1][j] != 1:
                                perimeter += 1
                        elif i == len(grid) - 1:
                            if grid[i - 1][j] != 1:
                                perimeter += 1
                        elif j == 0:
                            if grid[i][j + 1] != 1:
                                perimeter += 1
                        elif j == len(grid[i]) - 1:
                            if grid[i][j - 1] != 1:
                                perimeter += 1
                    else:
                        if grid[i + 1][j] != 1:
                            perimeter += 1
                        if grid[i - 1][j] != 1:
                            perimeter += 1
                        if grid[i][j + 1] != 1:
                            perimeter += 1
                        if grid[i][j - 1] != 1:
                            perimeter += 1
        return perimeter


s = Solution()
print s.islandPerimeter([[0, 1, 0, 0],
                         [1, 1, 1, 0],
                         [0, 1, 0, 0],
                         [1, 1, 0, 0]])
