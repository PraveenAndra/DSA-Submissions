class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        mat = [ ["."]*n for i in range(n)]
        res = []
        col = [0]*n
        left_diag = [0] * (2*n-1)
        right_diag = [0] * (2*n-1)
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board
        def backtrack(row,col,path):
            if row == n:
                res.append(create_board(path))
                return
            for i in range(n):
                if col[i] == 0 and left_diag[row + i]== 0 and right_diag[row-i]==0:
                    path[row][i] = 'Q'
                    col[i] = 1
                    left_diag[row+i] = 1
                    right_diag[row-i] = 1
                    backtrack(row+1,col,path)
                    path[row][i] = "."
                    col[i] = 0
                    left_diag[row+i] = 0
                    right_diag[row-i] = 0

        
        backtrack(0,col,mat)
        return res
            




            