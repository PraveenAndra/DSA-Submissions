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
            
            for i in range(up+1,down+1):
                res.append(matrix[i][right])
            
            if up != down:
                for i in range(right-1,left-1,-1):
                    res.append(matrix[down][i])
            
            if left!=right:
                for i in range(down-1,up,-1):
                    res.append(matrix[i][left])
            up += 1       
            left += 1
            down -= 1
            right -= 1
        return res

            

        