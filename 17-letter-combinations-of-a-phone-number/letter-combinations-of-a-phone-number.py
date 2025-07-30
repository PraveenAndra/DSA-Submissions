class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numMap = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        def backtrack(ind,curr):
            if ind == len(digits):
                res.append(curr)
                return
            for i in numMap[digits[ind]]:
                backtrack(ind+1,curr+i)
        if digits == "":
            return []
        backtrack(0,"")
        return res


        