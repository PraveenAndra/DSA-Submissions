class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        count = len(s)
        for i in range(len(s)-1):
            if s[i]== s[i+1]:
                count += 1
                dp[i][i+1] = True
        for diff in range(2,len(s)):
            for i in range(len(s)-diff):
                j = i+diff
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    count += 1
        return count


        