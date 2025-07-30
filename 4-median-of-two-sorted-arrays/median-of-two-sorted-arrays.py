class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2,nums1)
        
        l1,l2 = len(nums1), len(nums2)
        left = 0
        right = l1
        while left <= right:
            mid1 = (left+right)//2
            mid2 = (l1+l2+1)//2 - mid1
            max1 = float('-inf') if mid1 == 0 else nums1[mid1-1]
            max2 = float('-inf') if mid2 == 0 else nums2[mid2-1]
            min1 = float('inf') if mid1 == l1 else nums1[mid1]
            min2 = float('inf') if mid2 == l2 else nums2[mid2]
            if max1 <= min2 and max2 <= min1:
                if (l1+l2)%2 == 0:
                    return (max(max1,max2)+min(min1,min2))/2
                else:
                    return max(max1,max2)
            elif max1 > min2:
                right = mid1 - 1
            else:
                left = mid1+1
         