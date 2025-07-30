class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtrack(open,closed,curr):
            if len(curr) == 2*n:
                res.append(curr)
                return
            if open < n:
                backtrack(open+1,closed,curr+"(")
            if closed < open:
                backtrack(open,closed+1,curr+")")
        backtrack(0,0,"")
        return res


        