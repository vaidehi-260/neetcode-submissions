class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        perm=[]
        used=[False]*len(nums)
        def backtrack():
            if len(perm)==len(nums):
                ans.add(tuple(perm))
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                perm.append(nums[i])
                used[i]=True
                backtrack()
                perm.pop()
                used[i]=False
        backtrack()
        return [list(x) for x in ans]
            