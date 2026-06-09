class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        tmp=[]
        for i in range(n-k, n):
            tmp.append(nums[i])
        for i in range(n-k):
            tmp.append(nums[i])
        for i in range(n):
            nums[i]=tmp[i]
        return