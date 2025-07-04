class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        heapq.heappush(heap,(grid[0][0],0,0))
        seen = {(0,0)}
        while heap:
            val,r,c = heapq.heappop(heap)
            if r == len(grid)-1 and c == len(grid[0])-1:
                return val
            for i,j in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr,nc = r+i,c+j
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and (nr,nc) not in seen:
                    heapq.heappush(heap,(max(val,grid[nr][nc]),nr,nc))
                    seen.add((nr,nc))
        return -1
                
        