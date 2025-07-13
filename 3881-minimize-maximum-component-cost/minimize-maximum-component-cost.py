class DisjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
    def findParent(self,curr):
        if self.parent[curr]!= curr:
            self.parent[curr] = self.findParent(self.parent[curr])
        return self.parent[curr]

    def union(self,node1,node2):
        par1 = self.findParent(node1)
        par2 = self.findParent(node2)
        if par1 == par2:
            return False
        self.parent[node1] = node2
        return True
class Solution:
    
    # def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
    #     if n<=k:
    #         return 0
    #     edges.sort(key = lambda x:x[2])
    #     ds = DisjointSet(n)
    #     ans = n
    #     for u,v,w in edges:
    #         if ds.union(u,v):
    #             ans-=1
    #         if ans<=k:
    #             return w
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        def find(x):
            if x == f[x]:
                return x
            f[x] = find(f[x])
            return f[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return False
            f[x] = y
            return True

        if n <= k:
            return 0
        edges.sort(key = lambda e: e[2])
        count = n
        f = list(range(n))
        for u, v, w in edges:
            if union(u, v):
                count -= 1
            if count <= k:
                return w
        
        