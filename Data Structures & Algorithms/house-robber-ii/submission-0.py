class Solution:
    def rob(self, nums: List[int]) -> int:

        # Edge case: only one house
        if len(nums) == 1:
            return nums[0]

        # Function to solve the linear House Robber problem
        def helper(arr):
            memo = [-1] * len(arr)

            def dfs(i):
                if i >= len(arr):
                    return 0

                if memo[i] != -1:
                    return memo[i]

                rob = arr[i] + dfs(i + 2)
                skip = dfs(i + 1)

                memo[i] = max(rob, skip)
                return memo[i]

            return dfs(0)

        # Case 1: Ignore the last house
        case1 = helper(nums[:-1])

        # Case 2: Ignore the first house
        case2 = helper(nums[1:])

        return max(case1, case2)