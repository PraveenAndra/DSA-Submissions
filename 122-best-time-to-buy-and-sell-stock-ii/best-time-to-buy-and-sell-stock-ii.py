class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit = 0
        for price in prices:
            if price <= buy:
                buy = price
            else:
                profit += (price - buy)
                buy = price
        return profit
