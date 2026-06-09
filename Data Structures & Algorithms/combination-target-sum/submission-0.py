class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        sets = []
        def backtracking(i, total):
            if total == target:
                ans.append(sets[:])
                return
            if total>target:
                return
            if i == len(nums):
                return 
            sets.append(nums[i])
            backtracking(i, total+nums[i])

            sets.pop()
            backtracking(i+1, total)

        backtracking(0,0)
        return ans