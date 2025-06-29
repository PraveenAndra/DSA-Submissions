class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2                 # cut in nums1
            j = (m + n + 1)//2 - i             # matching cut in nums2

            L1 = -float('inf') if i == 0 else nums1[i-1]
            R1 =  float('inf') if i == m else nums1[i]
            L2 = -float('inf') if j == 0 else nums2[j-1]
            R2 =  float('inf') if j == n else nums2[j]

            if L1 <= R2 and L2 <= R1:           # correct partition
                if (m + n) & 1:                # odd length
                    return float(max(L1, L2))
                return (max(L1, L2) + min(R1, R2)) / 2.0
            elif L1 > R2:                      # move cut in nums1 left
                hi = i - 1
            else:                              # move cut in nums1 right
                lo = i + 1

        return -1.0 



        