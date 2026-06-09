class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l<r:
            mid = (l+r)//2
            day_need = 1
            curr_w = 0
            for w in weights:
                if curr_w + w>mid:
                    day_need+=1
                    curr_w=0
                curr_w+=w
            if day_need<=days:
                r = mid
            else:
                l = mid+1
        return l  