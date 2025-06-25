class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x,y):
            for i,j in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx,ny = x+i, y+j
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == "1":
                    grid[nx][ny] = "0"
                    dfs(nx,ny)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    res += 1
        return res
                


                

        
             



        
         
        
        