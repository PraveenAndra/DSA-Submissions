class Solution:
    def makeFancyString(self, s: str) -> str:
        currChar = s[0]
        currCount = 1
        res = ""
        for i in s[1:]:
            if i == currChar:
                currCount += 1
            else:
                res += currChar*currCount if currCount <=2 else currChar*2
                currChar = i
                currCount = 1
        res += currChar*currCount if currCount <=2 else currChar*2
        return res
            
        