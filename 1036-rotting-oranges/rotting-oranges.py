class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
        res = 0
        while q:
            for i in range(len(q)):
                x,y = q.popleft()
                for r,c in [(0,1),(1,0),(-1,0),(0,-1)]:
                    nx,ny = x+r,y+c
                    if 0<= nx < len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx,ny))
            res += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return max(res-1,0)




        
        