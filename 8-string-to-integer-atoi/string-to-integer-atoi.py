class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i< len(s) and s[i] == " ":
            i += 1
        sign = False
        if i < len(s) and s[i] == "-":
            sign = True
            i += 1
        elif i<len(s) and s[i] == "+":
            i += 1
        res = 0
        while i<len(s) and s[i].isdigit():
            res = res*10 + int(s[i])
            i+=1
        return max(-res,-2**31) if sign else min(res,2**31-1) 
        

        