class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(len(nums)):
            curr = nums[i]
            ans = max(ans, curr)
            for j in range(i+1, len(nums)):
                curr *=nums[j]
                ans = max(ans, curr)

        return ans