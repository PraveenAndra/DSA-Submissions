class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # top-down

        # def checkMove(x,y,curr):
        #     if curr == 0:


        #Bottom - up
        rows = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(2,-1),(1,2),(2,1)]
        prev_dp = [[0]*n for i in range(n)]
        curr_dp = [[0]*n for i in range(n)]
        prev_dp[row][column] = 1
        for moves in range(1,k+1):
            for i in range(n):
                for j in range(n):
                    curr_dp[i][j] = 0
                    for x,y in rows:
                        nx,ny = i+x,j+y
                        if 0<=nx<n and 0<=ny<n:
                            curr_dp[i][j] += prev_dp[nx][ny] / 8
            prev_dp,curr_dp = curr_dp,prev_dp
        total_prob = sum(prev_dp[i][j] for i in range(n) for j in range(n))
        return total_prob



        