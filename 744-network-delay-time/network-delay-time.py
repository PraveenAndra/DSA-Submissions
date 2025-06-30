class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = defaultdict(list)
        covered = set()
        for u,v,w in times:
            nodes[u].append((w,v))
        q = [(0,k)]
        while q:
            time, node = heapq.heappop(q)
            covered.add(node)
            if len(covered) == n:
                return time
            for j,k in nodes[node]:
                if k not in covered:
                    heapq.heappush(q,(time+j,k))
            
            
        return -1

        
        
        