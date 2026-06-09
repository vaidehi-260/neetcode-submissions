class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = len(nums)+1
        for i in range(len(nums)):
            count, arr = 0, []
            for j in range(i, len(nums)):
                arr.append(nums[j])
                count += nums[j]
                if count >= target:
                    minlen = min(minlen, len(arr))
                    break
        if minlen<=len(nums):
            return minlen
        else:
            return 0

