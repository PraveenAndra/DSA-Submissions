class DisjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(0,n+1)]
        self.rank = [0]*(n+1)
    def find(self,node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self,A,B):
        rootA = self.find(A)
        rootB = self.find(B)
        if rootA == rootB:
            return True
        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = self.parent[rootB]
            self.rank[rootB] += 1
        else:
            self.parent[rootB] = self.parent[rootA]
            self.rank[rootA] += 1
        return False
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = []
        dsu = DisjointSet(len(edges))
        for i,j in edges:
            if dsu.union(i,j):
                res = [i,j]
        return res

        