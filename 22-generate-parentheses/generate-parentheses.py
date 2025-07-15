class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(ind,arr,openCount,closedCount):
            if ind == 2*n:
                res.append(''.join(arr))
            if openCount==0:
                arr.append("(")
                backtrack(ind+1,arr,openCount+1,closedCount)
            else:
                if openCount < n:
                    arr.append("(")
                    backtrack(ind+1,arr,openCount+1,closedCount)
                    arr.pop()
                if closedCount < openCount:
                    arr.append(")")
                    backtrack(ind+1,arr,openCount,closedCount+1)
                    arr.pop()
        backtrack(0,[],0,0)
        return res
            

        