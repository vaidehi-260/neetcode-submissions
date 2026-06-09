class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(maxsum):
            sub_arr = 1
            curr_sum = 0
            for n in nums:
                if curr_sum + n >maxsum:
                    sub_arr+=1
                    curr_sum = n
                else:
                    curr_sum += n
            return sub_arr<=k
        l, r = max(nums), sum(nums)
        ans = r
        while l<=r:
            mid = (l+r)//2
            if cansplit(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
