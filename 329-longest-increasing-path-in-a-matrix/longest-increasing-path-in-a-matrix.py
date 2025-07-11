class Solution:
    def dfs(self, matrix, r, c, dp):
        if dp[r][c]:
            return dp[r][c]
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        longest_path = 0
        for d in directions:
            new_r, new_c = r + d[0], c + d[1]
            if 0 <= new_r < m and 0 <= new_c < n \
                    and matrix[new_r][new_c] > matrix[r][c]:
                longest_path = max(longest_path, self.dfs(matrix, new_r, new_c, dp))
        dp[r][c] = 1 + longest_path
        return dp[r][c]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        return max(self.dfs(matrix, r, c, dp) for r in range(m) for c in range(n))