class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        dp = [[False for i in range(l)] for i in range(l)]
        # print(dp)
        count = l
        for i in range(l):
            dp[i][i] = True

        for i in range(l-1):
            if s[i]==s[i+1]:
                count += 1
                dp[i][i+1] = True
        for diff in range(2,l):
            for i in range(l-diff):
                j = i+diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    count += 1
        return count
                 
        