class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        q1,q2 = deque(),deque()
        for i in range(len(heights)):
            q1.append((i, 0))
            q2.append((i, len(heights[0]) - 1))
        for i in range(len(heights[0])):
            q1.append((0, i))
            q2.append((len(heights) - 1, i))
        
        def bfs(q):
            res = set()
            while q:
                r,c = q.popleft()
                res.add((r,c))
                for i,j in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nr,nc = r+i,c+j
                    if 0<=nr<len(heights) and 0<=nc<len(heights[0]) and (nr,nc) not in res and heights[nr][nc] >= heights[r][c]:
                        q.append((nr,nc))
            return res
        pacific = bfs(q1)
        atlantic = bfs(q2)
        return list(pacific.intersection(atlantic))



        