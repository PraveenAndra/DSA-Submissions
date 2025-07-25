class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l,r = m-1,n-1
        for i in range(m+n-1, -1, -1):
            if r < 0 or l < 0:
                break
            if nums2[r] >= nums1[l]:
                nums1[i] = nums2[r]
                r -= 1
            else:
                nums1[i] = nums1[l]
                l -= 1
        for i in range(r+1):
            nums1[i] = nums2[i]
        