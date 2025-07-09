class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(m):
            temp = [0]*(n+1)
            for j in range(1,n+1):
                temp[j] = temp[j-1]+dp[j]
            dp = temp
        return dp[n]
                

                
        