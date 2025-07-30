class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # left_max = [0]*(n+1)
        # right_max = [0]*(n+1)
        # for i in range(len(height)):
        #     left_max[i] = max(left_max[i-1],height[i])
        # for i in range(len(height)-1,-1,-1):
        #     right_max[i] = max(right_max[i+1],height[i])
        # res = 0
        # for i in range(len(height)):
        #     res += abs(height[i] - min(left_max[i],right_max[i]))
        # return res
        left = 0
        right = len(height)-1
        left_max,right_max = 0,0
        res = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max,height[left])
                res += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max,height[right])
                res += right_max - height[right]
                right -= 1
        return res




        