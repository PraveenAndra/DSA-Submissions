class DisjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
        self.comps = 0
    def find(self,node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self,node1,node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 != parent2:
            if self.rank[parent1] < self.rank[parent2]:
                self.parent[parent1] = self.parent[parent2]
            elif self.rank[parent1] > self.rank[parent2]:
                self.parent[parent2] = self.parent[parent1]
            else:
                self.rank[parent1] += 1
                self.parent[parent2] = self.parent[parent1]
            self.comps += 1
            return True
        return False
    


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        dsu = DisjointSet(n)

        for i,j in edges:
            dsu.union(i,j)
                # n-=1
        print(dsu.comps)
        return n - dsu.comps

        