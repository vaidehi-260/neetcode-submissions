class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num = sorted(num)
        total = len(nums1)+len(nums2)
        if (total)%2 == 0:
            return (num[(total//2)-1] + num[total//2])/2
        else:
            return num[total//2]