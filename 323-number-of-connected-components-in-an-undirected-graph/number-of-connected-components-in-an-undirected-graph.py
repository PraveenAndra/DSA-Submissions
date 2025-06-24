class DisjoinSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
    
    def find(self,n):
        if n!=self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    def union(self,A,B):
        rootA = self.find(A)
        rootB = self.find(B)
        if rootA == rootB:
            return 0
        if self.size[rootA] < self.size[rootB]:
            self.size[rootB] += self.size[rootA]
            self.parent[rootA] = rootB
        else:
            self.size[rootA] += self.size[rootB]
            self.parent[rootB] = rootA
        return 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Iterative DFS
        # adj_mat = defaultdict(list)
        # for i,j in edges:
        #     adj_mat[i].append(j)
        #     adj_mat[j].append(i)
        # visited = [False]*n
        # def iter_dfs(node,visited,adj_mat):
        #     stack = [node]
        #     visited[node] = True
        #     for i in adj_mat[node]:
        #         if not visited[i]:
        #             iter_dfs(i,visited,adj_mat)
        #     return
        # res = 0
        # for i in range(n):
        #     if not visited[i]:
        #         iter_dfs(i,visited,adj_mat)
        #         res += 1
        
        # return res

        #DSU
        dsu1 = DisjoinSet(n)
        dsu2 = DisjoinSet(n)
        res = n
        for i,j in edges:
            res -= dsu1.union(i,j)
        return res
            




        