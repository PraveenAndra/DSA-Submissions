class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        maxArea = 0
        for i in range(len(heights)):
            while stack[-1]!=-1 and heights[stack[-1]] >= heights[i]:
                curr_height = heights[stack.pop()]
                curr_width = i-stack[-1]-1
                maxArea = max(maxArea,curr_height*curr_width)
            stack.append(i)
        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            maxArea = max(maxArea, current_height * current_width)
        return maxArea