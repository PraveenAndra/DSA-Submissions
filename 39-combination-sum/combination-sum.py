class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(ind,curr,target):
            if target==0:
                res.append(curr[:])
                return
            for i in range(ind,len(candidates)):
                if candidates[i] <= target:
                    curr.append(candidates[i])
                    backtrack(i,curr,target-candidates[i])
                    curr.pop()
        backtrack(0,[],target)
        return res

