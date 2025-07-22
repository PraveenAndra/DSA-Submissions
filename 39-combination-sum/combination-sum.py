class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        def backtrack(rem,curr,start):
            # if ind == len(candidates):
            #     return
            if rem == 0:
                res.append(curr[:])
                return
            for num in range(start,len(candidates)):
                if rem-candidates[num] >= 0:
                    curr.append(candidates[num])
                    backtrack(rem-candidates[num],curr,num)
                    curr.pop()
        backtrack(target,[],0)
        return res
        