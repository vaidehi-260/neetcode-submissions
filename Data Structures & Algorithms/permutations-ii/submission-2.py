class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        perm=[]
        used = [False]*len(nums)
        def backtrack():
            if len(perm)==len(nums):
                ans.append(perm[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                perm.append(nums[i])
                used[i]=True
                backtrack()
                perm.pop()
                used[i]=False
        backtrack()
        return ans