class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0]*len(s) for i in range(len(s))]
        res = [None,None]
        for i in range(len(s)):
            dp[i][i] = 1
            res = [i,i]
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = 1
                res = [i,i+1]
        for diff in range(2,len(s)):
            for i in range(len(s)-diff):
                j = i+diff
                if s[i] ==s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                    res = [i,j]
        return s[res[0]:res[1]+1]
                


        