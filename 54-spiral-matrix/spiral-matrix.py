class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top = 0
        bottom = len(matrix) - 1
        right = len(matrix[0])-1
        left = 0
        while len(res) < len(matrix)*len(matrix[0]):
            # Move right
            for i in range(left,right+1):
                res.append(matrix[top][i])
            
            for i in range(top+1,bottom +1):
                res.append(matrix[i][right])
            if top != bottom:
                for i in range(right-1,left-1,-1):
                    res.append(matrix[bottom][i])
            if left != right:
                for i in range(bottom-1,top,-1):
                    res.append(matrix[i][left])
            bottom -= 1
            right -= 1
            top += 1
            left += 1
        return res

        