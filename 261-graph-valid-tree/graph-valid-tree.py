class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)
        seen = {0}
        stack = [0]
        while stack:
            node = stack.pop()
            for k in adj_list[node]:
                if k not in seen:
                    stack.append(k)
                    seen.add(k)
        print(seen)
        return len(seen) == n
