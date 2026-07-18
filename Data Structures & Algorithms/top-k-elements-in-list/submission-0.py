class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = 1+ freq.get(i, 0)
        ans=[]
        for num, i in freq.items():
            ans.append([i, num])
        ans.sort()
        res=[]
        while len(res)<k:
            res.append(ans.pop()[1])
        return res
        