class Solution:
    def numDecodings(self, s: str) -> int:
        one_back = 1
        two_back = 1
        dp = [0]*len(s)
        dp[0] = 1
        if s[0]=="0":
            return 0
        for i in range(1,len(s)):
            curr = 0
            if s[i]!="0":
                curr = one_back
            if s[i-1]!="0":
                if 10 <= int(s[i-1:i+1]) <= 26:
                    curr += two_back 
            two_back = one_back
            one_back = curr
        return one_back
            
            


