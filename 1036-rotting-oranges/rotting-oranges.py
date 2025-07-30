class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshOranges = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        time = 0
        while q:
            for i in range(len(q)):
                x,y  = q.popleft()
                for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                    nx,ny = x+a,y+b
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == 1:
                        freshOranges -= 1
                        grid[nx][ny] = 2
                        q.append((nx,ny))
                        
            time += 1
        
        return max(time-1,0) if freshOranges == 0 else -1


        