class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
    
        # Number of rows and columns
        rows, cols = len(matrix), len(matrix[0])
        
        # Initialize the height array
        heights = [0] * cols
        max_area = 0
        
        # Function to calculate the maximal rectangle in a histogram
        def largestRectangleInHistogram(heights):
            stack = []
            max_area = 0
            for i in range(len(heights) + 1):
                # We add a 0 at the end to pop out remaining bars
                h = 0 if i == len(heights) else heights[i]
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
            return max_area
        
        # Process each row of the matrix
        for row in matrix:
            for i in range(cols):
                # Update the height of each column (if the value is '1', increase height, else reset to 0)
                heights[i] = heights[i] + 1 if row[i] == "1" else 0
            
            # For the current heights array, calculate the maximum area rectangle
            max_area = max(max_area, largestRectangleInHistogram(heights))
        
        return max_area