class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)==1 and len(grid[0]) == 1:
            return grid[0][0]
        heap = []
        heapq.heappush(heap,(grid[0][0],(0,0)))
        visited = set()
        while heap:
            path_sum, point = heapq.heappop(heap)
            if point in visited:
                continue
            visited.add(point)
            for i,j in [(0,1),(1,0)]:
                nr,nc = point[0]+i,point[1]+j
                if 0 <= nr< len(grid) and 0<=nc<len(grid[0]):
                    if (nr,nc) == (len(grid)-1,len(grid[0])-1):
                        return path_sum+grid[nr][nc]
                    heapq.heappush(heap,(grid[nr][nc]+path_sum,(nr,nc)))
        return -1
                
        