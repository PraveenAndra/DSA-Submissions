class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(ind,curr,s):
            if s== target:
                res.append(curr[:])
                return
            if ind >= len(candidates) or s > target:
                return
        
            for i in range(ind,len(candidates)):
                if i != ind and candidates[i] == candidates[i-1]:
                    continue 
                curr.append(candidates[i])
                dfs(i+1,curr,s+candidates[i])
                curr.pop()
        
        candidates.sort()
        dfs(0,[],0)
        return res