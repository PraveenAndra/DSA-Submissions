class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for i in range(n)]
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        curr_ind = 0
        r,c = 0,0
        borders = [0,n-1,0,n-1]
        for i in range(1,n**2+1):
            matrix[r][c] = i
            dx,dy = dir[curr_ind]
            if (r+dx < 0 or r+dx >=n or c+dy <0 or c+dy >=n) or (matrix[r+dx][c+dy] > 0):
                curr_ind = (curr_ind +1) % 4
            dx,dy = dir[curr_ind]
            r,c = r+dx,c+dy
        return matrix   
        