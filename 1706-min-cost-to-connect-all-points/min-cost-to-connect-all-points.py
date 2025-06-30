class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        q = []
        q.append((0,0))
        visited = [0]*N
        min_dist = [0]*N
        cost = 0
        while q:
            res, point = heapq.heappop(q)
            if visited[point] !=0:
                continue
            cost += res
            visited[point] = 1
            for dist,j in adj[point]:
                if visited[j] == 0:
                    heapq.heappush(q,(dist,j))
        return cost
                
            


        