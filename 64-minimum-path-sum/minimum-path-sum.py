class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j==0:
                    continue
                if j == 0:
                    grid[i][j] += grid[i-1][j]
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                else:
                    grid[i][j] += min(grid[i][j-1],grid[i-1][j])
        return grid[-1][-1]
        