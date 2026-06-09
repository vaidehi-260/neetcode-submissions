class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set ()
        n = len(nums)
        for i in range(n):
            if nums[i] in seen:
                return nums[i]
            seen.add(nums[i])
        return -1
