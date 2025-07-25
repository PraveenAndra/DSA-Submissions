class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        res = 0
        for price in prices:
            buy = min(buy,price)
            res = max(res,price-buy)
        return res
        