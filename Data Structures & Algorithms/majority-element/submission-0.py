class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums)//2
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        maxm=0
        for j in freq:
            if freq[j]>maj:
                maxm = max(maxm, j)
        return maxm