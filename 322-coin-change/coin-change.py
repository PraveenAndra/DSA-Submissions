class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def backtrack(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if rem in memo:
                return memo[rem]
            min_cost = float('inf')
            for coin in coins:
                res = backtrack(rem - coin)
                if res != -1:
                    min_cost = min(min_cost,res+1)
            memo[rem] = min_cost if min_cost!= float('inf') else -1
            return memo[rem]
        return backtrack(amount)
        # counter = [float('inf')]* (amount+1)
        # counter[0] = 0
        # for i in coins:
        #     for j in range(i,amount+1):
        #         counter[j] = min(counter[j],counter[j-i]+1)
        # return counter[amount] if counter[amount]!=float('inf') else -1
        
        