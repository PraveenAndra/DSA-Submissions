class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        i,j = 0,0
        r,c = len(matrix),len(matrix[0])
        res = []
        up,down,left,right = 0,r-1,0,c-1
        while len(res) < r*c:
            # Top row
            for j in range(left,right+1):
                res.append(matrix[up][j])
            # Right Col
            up += 1
            for i in range(up,down+1):
                res.append(matrix[i][right])
            right -= 1
            if up -1 != down:
                for i in range(right,left-1,-1):
                    res.append(matrix[down][i])
            down -= 1
            if left!=right+1:
                for i in range(down,up-1,-1):
                    res.append(matrix[i][left])
            left += 1
        return res

            

        