class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        dp = [[0]*(amount+1) for i in range(len(coins))]
        # def dfs(ind,amount):
        #     nonlocal res
        #     if amount == 0:
        #         return 1
        #     if ind == len(coins):
        #         return 0
        #     if dp[ind][amount] != -1:
        #         return dp[ind][amount]
        #     if coins[ind] > amount:
        #         dp[ind][amount] = dfs(ind+1,amount)
        #     else:
        #         dp[ind][amount] = dfs(ind,amount-coins[ind])+dfs(ind+1,amount)
        #     return dp[ind][amount]
        # return dfs(0,amount)
        for i in range(len(coins)):
            dp[i][0] = 1
            for j in range(1,amount+1):
                if coins[i] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][amount]
         
            
        