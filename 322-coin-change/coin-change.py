class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        @lru_cache(None)
        def dfs(amt):
            if amt < 0:
                return -1
            if amt == 0:
                return 0
            m = float('inf')
            for coin in coins:
                r = dfs(amt-coin)
                if r!=-1:
                    m = min(m,r+1)
            return m if m!= float('inf') else -1

        return dfs(amount)


            
        