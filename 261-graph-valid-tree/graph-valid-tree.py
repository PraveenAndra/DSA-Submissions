class DisjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
    def find(self,A):
        if self.parent[A]!= A:
            self.parent[A] = self.find(self.parent[A])
        return self.parent[A]
    def union(self,node1,node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 != parent2:
            if self.rank[parent1] < self.rank[parent2]:
                self.parent[parent1] = self.parent[parent2]
            elif self.rank[parent2] < self.rank[parent1]:
                self.parent[parent2] = self.parent[parent1]
            else:
                self.parent[parent2] = self.parent[parent1]
                self.rank[parent1] += 1
            return True
        else:
            return False

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ds = DisjointSet(n)
        if len(edges)< n -1:
            return False
        for i,j in edges:
            if not ds.union(i,j):
                return False
        return True
        
        