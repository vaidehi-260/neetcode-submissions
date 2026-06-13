class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total%k:
            return False
        target = total//k
        nums.sort(reverse=True)
        sides = [0]*k
        def dfs(index):
            if index == len(nums):
                return True
            stick = nums[index]
            for i in range(k):
                if stick+sides[i]>target:
                    continue
                sides[i]+=stick
                if dfs(index+1):   # to check whether future me current arrangement successful hoga ya nhi
                    return True 
                sides[i]-=stick
                if sides[i]==0:
                    break
            return False
        return dfs(0)