class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k==0:
            return 1
        next_dp = [[0]*n for i in range(n)]
        curr_dp = [[0]*n for i in range(n)]
        curr_dp[row][column] = 1
        possible_moves = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,-2),(2,-1),(1,2),(2,1)]
        for moves in range(k):
            for i in range(n):
                for j in range(n):
                    for r,c in possible_moves:
                        nx,ny = i+r,j+c
                        if 0 <= nx < n and 0<=ny<n:
                            next_dp[nx][ny] += curr_dp[i][j] / 8
            curr_dp = next_dp
            next_dp = [[0]*n for i in range(n)]
                         
        return sum(curr_dp[i][j] for i in range(n) for j in range(n))




        