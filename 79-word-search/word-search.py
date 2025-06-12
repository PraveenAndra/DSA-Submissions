class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(x,y,visited,ind):
            if ind == len(word):
                return True
            for i,j in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx,ny = x+i,j+y
                if 0<=nx<len(board) and 0<=ny<len(board[0]) and (nx,ny) not in visited and word[ind] == board[nx][ny]:
                    visited.add((nx,ny))
                    if backtrack(nx,ny,visited,ind+1):
                        return True
                    visited.remove((nx,ny))
            return False


        stack = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                visited.add((i,j))
                if board[i][j] == word[0] and backtrack(i,j,visited,1):
                    return True
        return False

        