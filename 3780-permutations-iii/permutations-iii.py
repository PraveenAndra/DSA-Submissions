class Solution:
    def permute(self, n: int) -> List[List[int]]:
        res = []
        def backtrack(curr,visited):
            if len(curr) == n:
                res.append(curr[:])
                return
            last = curr[-1]
            for i in range(1,n+1):
                if i not in visited and i%2 != last%2:
                    curr.append(i)
                    visited.add(i)
                    backtrack(curr,visited)
                    curr.pop()
                    visited.remove(i)
        
        for i in range(1,n+1):
            backtrack([i],{i})
        return res

        