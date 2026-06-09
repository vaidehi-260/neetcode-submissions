class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        l, r = 0, 1
        while r<n:
            if prices[l]<prices[r]:
                p = prices[r]-prices[l]
                profit=max(p, profit)
            else:
                l=r
            r+=1
        return profit
