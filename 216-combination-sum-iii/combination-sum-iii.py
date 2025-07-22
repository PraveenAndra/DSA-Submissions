class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(rem,curr,ind):
            
            if rem==0 and len(curr) == k:
                res.append(curr[:])
                return 
            if rem < 0 or len(curr) == k:
                return
            for i in range(ind,10):
                curr.append(i)
                dfs(rem-i,curr,i+1)
                curr.pop()
        
        dfs(n,[],1)
        return res
            
        