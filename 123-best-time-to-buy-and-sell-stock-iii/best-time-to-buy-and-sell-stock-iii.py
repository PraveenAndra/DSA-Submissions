class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost,t1_profit = float('inf'),0
        t2_cost,t2_profit = float('inf'),0
        for price in prices:
            t1_cost = min(t1_cost,price)
            t1_profit = max(t1_profit,price - t1_cost)
            t2_cost = min(t2_cost,price-t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)
        return t2_profit