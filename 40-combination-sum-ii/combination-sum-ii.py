class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(ind,rem,curr):
            if rem < 0:
                return 
            if rem == 0:
                res.append(curr[:])
                return
            for i in range(ind,len(candidates)):
                if i>ind and candidates[i] == candidates[i-1]:
                    continue
                if rem < candidates[i]:
                    continue
                curr.append(candidates[i])
                dfs(i+1,rem- candidates[i],curr)
                curr.pop()

        candidates.sort()
        dfs(0,target,[])
        return res