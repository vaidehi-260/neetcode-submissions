class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums = sorted(nums)
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return True
            elif nums[m]>target:
                r = m-1
            else:
                l = m+1
        return False