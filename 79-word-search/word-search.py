class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(x,y,ind):
            if ind == len(word):
                return True
            val = board[x][y]
            board[x][y] = "#"
            for i,j in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx,ny = x+i,y+j
                if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny] == word[ind]:
                
                    if search(nx,ny,ind+1):
                        return True
            board[x][y] = val
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(i,j,1):
                        return True
        return False
