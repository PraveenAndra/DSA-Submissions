class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        adj_list = [[] for i in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        q = deque([0])
        seen = {0}
        while q:
            curr = q.popleft()
            for i in adj_list[curr]:
                if i in seen:
                    continue
                seen.add(i)
                q.append(i)
        return len(seen) == n


        