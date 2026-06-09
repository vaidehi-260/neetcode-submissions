class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        def backtrack(i, curr_xor):
            nonlocal ans
            if i == len(nums):
                ans+=curr_xor
                return 
            backtrack(i+1, curr_xor^nums[i])
            backtrack(i+1, curr_xor)

        backtrack(0, 0)
        return ans