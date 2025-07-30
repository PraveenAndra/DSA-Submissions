class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        dp = [[-1]*(amount+1) for i in range(len(coins))]
        def dfs(ind,amount):
            nonlocal res
            if amount == 0:
                return 1
            if ind == len(coins):
                return 0
            if dp[ind][amount] != -1:
                return dp[ind][amount]
            if coins[ind] > amount:
                dp[ind][amount] = dfs(ind+1,amount)
            else:
                dp[ind][amount] = dfs(ind,amount-coins[ind])+dfs(ind+1,amount)
            return dp[ind][amount]
        return dfs(0,amount)
         
            
        