class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit = 0
        for i in prices:
            buy = min(buy,i)
            profit = max(profit, i-buy)
        return profit

        