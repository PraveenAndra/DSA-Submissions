class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        dp = [[False]*l for i in range(l)]
        ans = [0,0]
        for i in range(l):
            dp[i][i] = True
        for i in range(l-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i,i+1]
        for diff in range(2,l):
            for i in range(l-diff):
                j = i+diff
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i,j]
        i,j = ans
        return s[i:j+1]

