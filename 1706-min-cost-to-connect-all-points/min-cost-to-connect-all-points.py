class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        heap = [(0,0)]
        visited = [False]*n
        cost = 0
        edges = 0
        while edges < n:
            weight,node = heapq.heappop(heap)
            if visited[node]:
                continue
            visited[node] = True
            cost += weight
            edges += 1
            for next in range(n):
                if not visited[next]:
                    next_weight = abs(points[node][0] - points[next][0]) + abs(points[node][1] - points[next][1])
                    heapq.heappush(heap,(next_weight,next))
        
        return cost