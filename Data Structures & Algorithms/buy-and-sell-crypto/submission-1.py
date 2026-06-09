class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minbuy=prices[0]
        for sell in prices:
            profit = max(profit, sell-minbuy)
            minbuy=min(minbuy, sell)
        return profit