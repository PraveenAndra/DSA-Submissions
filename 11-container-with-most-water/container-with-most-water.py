class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Brute Force(TLE)
        # res = 0
        # for i in range(len(height)):
        #     for j in range(i,len(height)):
        #         area = min(height[i],height[j]) * (j-i)
        #         res = max(res,area)
        # return res

        #Two Pointer
        left,right = 0 ,len(height)-1
        res = 0
        while left < right:
            area = min(height[left],height[right]) * (right-left)
            res = max(res,area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
            