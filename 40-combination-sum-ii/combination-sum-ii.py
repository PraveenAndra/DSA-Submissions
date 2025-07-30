class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(ind,curr,target):
            nonlocal res
            if target == 0:
                res.append(curr[:])
                return
            if ind >= len(candidates):
                return
            for i in range(ind,len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] <= target:
                    curr.append(candidates[i])
                    backtrack(i+1,curr,target-candidates[i])
                    curr.pop()
        backtrack(0,[],target)
        return res
