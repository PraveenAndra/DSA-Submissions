class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        rows = [set() for i in range(N)]
        cols = [set() for i in range(N)]
        boxes = [set() for i in range(N)]
        for i in range(N):
            for j in range(N):
                num = board[i][j]
                if num == ".":
                    continue
                if num in rows[i]:
                    return False
                if num in cols[j]:
                    return False
                if num in boxes[(i//3)*3+j//3]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[(i//3)*3+j//3].add(num)
        return True
        