class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def solve(x):
            if x ==0:
                return 0
            if x <0:
                return float('inf')
            if x in dp:
                return dp[x]
            ans = float('inf')
            for c in coins:
                ans = min(ans, 1+solve(x-c))
            dp[x]=ans
            return ans
        ans = solve(amount)
        return -1 if ans == float('inf') else ans