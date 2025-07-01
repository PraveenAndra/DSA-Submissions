class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = float('inf')
        n = len(pattern)
        def backtrack(ind,curr,visited):
            nonlocal res
            if ind == n:
                res = min(res,curr)
                return 
            prev = curr % 10
            if pattern[ind] == "D":
                for i in range(1,prev):
                    if i not in visited:
                        visited.add(i)
                        backtrack(ind+1,curr*10+i,visited)
                        visited.remove(i)
            else:
                for i in range(prev+1,10):
                    if i not in visited:
                        visited.add(i)
                        backtrack(ind+1,curr*10+i,visited)
                        visited.remove(i)
                

        for i in range(1,10):
            backtrack(0,i,{i})
        return str(res)