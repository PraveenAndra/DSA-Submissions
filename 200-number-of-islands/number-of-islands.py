class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r,c = len(grid),len(grid[0])
        def traverseIsland(a,b):
            for i,j in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr,nc = a+i,b+j
                if 0<=nr<r and 0<=nc<c and grid[nr][nc] == "1":
                    grid[nr][nc] = 0
                    traverseIsland(nr,nc)
        islands = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    grid[i][j] = 0
                    traverseIsland(i,j)
                    islands += 1
        return islands


        