class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return 0
        pacific_nodes = deque()
        atlantic_nodes = deque()
        r,c = len(heights),len(heights[0])
        for i in range(r):
            pacific_nodes.append((i,0))
            atlantic_nodes.append((i,c-1))
        for i in range(c):
            pacific_nodes.append((0,i))
            atlantic_nodes.append((r-1,i))
        
        def check_cells(q):
            visited = set()
            while q:
                i,j = q.popleft()
                visited.add((i,j))
                for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                    ni,nj = i+a,j+b
                    if 0<=ni<len(heights) and 0<=nj<len(heights[0]) and heights[ni][nj] >= heights[i][j] and (ni,nj) not in visited:
                        q.append((ni,nj))
            return visited
        
        pacific = check_cells(pacific_nodes)
        atlantic = check_cells(atlantic_nodes)
        return list(pacific.intersection(atlantic))

