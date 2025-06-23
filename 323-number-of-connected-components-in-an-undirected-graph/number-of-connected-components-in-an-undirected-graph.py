class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_mat = defaultdict(list)
        for i,j in edges:
            adj_mat[i].append(j)
            adj_mat[j].append(i)
        visited = [False]*n
        def iter_dfs(node,visited,adj_mat):
            stack = [node]
            visited[node] = True
            for i in adj_mat[node]:
                if not visited[i]:
                    iter_dfs(i,visited,adj_mat)
            return
        res = 0
        for i in range(n):
            if not visited[i]:
                iter_dfs(i,visited,adj_mat)
                res += 1
        
        return res



        