class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #Djikistras
        # if len(grid)==1 and len(grid[0]) == 1:
        #     return grid[0][0]
        # heap = []
        # heapq.heappush(heap,(grid[0][0],(0,0)))
        # visited = set()
        # while heap:
        #     path_sum, point = heapq.heappop(heap)
        #     if point in visited:
        #         continue
        #     visited.add(point)
        #     for i,j in [(0,1),(1,0)]:
        #         nr,nc = point[0]+i,point[1]+j
        #         if 0 <= nr< len(grid) and 0<=nc<len(grid[0]):
        #             if (nr,nc) == (len(grid)-1,len(grid[0])-1):
        #                 return path_sum+grid[nr][nc]
        #             heapq.heappush(heap,(grid[nr][nc]+path_sum,(nr,nc)))
        # return -1
                
        # DP
        r,c = len(grid),len(grid[0])
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                if i==r-1 and j!=c-1:
                    grid[i][j] = grid[i][j] + grid[i][j+1]
                elif i!=r-1 and j==c-1:
                    grid[i][j] = grid[i][j] + grid[i+1][j]  
                elif i!=r-1 and j!=c-1:
                    grid[i][j] = grid[i][j] + min(grid[i+1][j],grid[i][j+1])
        return grid[0][0]
            
