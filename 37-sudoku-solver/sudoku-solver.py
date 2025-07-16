class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [defaultdict(int) for i in range(9)]
        cols = [defaultdict(int) for i in range(9)]
        boxes = [defaultdict(int) for i in range(9)]
        box_ind = lambda x,y: (x//3)*3 + (y//3) 
        def place_number(r,c,num):
            rows[r][num] += 1
            cols[c][num] += 1
            boxes[box_ind(r,c)][num] += 1
            board[r][c] = str(num)
        def can_place_number(r,c,num):
            if not (num in rows[r] or num in cols[c] or num in boxes[box_ind(r,c)]):
                return True
            return False
        def place_next(r,c):
            if c == 8 and r == 8:
                solved[0] = True
            else:
                if c==8:
                    backtrack(r+1,0)
                else:
                    backtrack(r,c+1)
        def remove_number(r,c,num):
            # rows[r][num] -= 1
            # cols[c][num] -=1 
            # boxes[box_ind(r,c)][num] -= 1
            # if rows[r][num] == 0:
            del rows[r][num]
            # if cols[c][num] == 0:
            del cols[c][num]
            # if boxes[box_ind(r,c)][num] == 0:
            del boxes[box_ind(r,c)][num]
            board[r][c] = "."
        def backtrack(r,c):
            if board[r][c] == ".":
                for num in range(1,10):
                    if can_place_number(r,c,num):
                        place_number(r,c,num)
                        place_next(r,c)
                        if solved[0]:
                            return
                        remove_number(r,c,num)
            else:
                place_next(r,c)

        

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    place_number(i,j,int(board[i][j]))
        solved = [False]
        backtrack(0,0)
