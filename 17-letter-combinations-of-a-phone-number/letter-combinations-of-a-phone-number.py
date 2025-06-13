class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        num_map = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        def backtrack(ind,curr):
            if ind == len(digits):
                res.append(curr)
                return
            for letter in num_map[int(digits[ind])]:
                backtrack(ind+1,curr+letter)
        if digits == "":
            return []
        backtrack(0,"")
        return res
        