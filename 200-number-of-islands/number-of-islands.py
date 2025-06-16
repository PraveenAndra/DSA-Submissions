class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(gridMap,x,y):
            q = deque()
            q.append((x,y))
            while q:
                a,b = q.popleft()
                for i,j in [(0,1),(-1,0),(0,-1),(1,0)]:
                    nx,ny = a+i,b+j
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and gridMap[nx][ny] == '1':
                        gridMap[nx][ny] = 0
                        q.append((nx,ny))
            return gridMap
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid[i][j] = 0
                    grid = bfs(grid,i,j)
                    res += 1
        return res

                

        
             



        
         
        
        