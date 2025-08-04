class Solution:
    def numTrees(self, n: int) -> int:
        def solve(n):
            if n <= 1:
                return 1
            
            if n in memo:
                return memo[n]
            
            ans = 0
            for i in range(1, n+1):
                left_options = solve( i - 1 )
                right_options = solve( n - i )
                ans += left_options * right_options
            
            memo[n] = ans
            return memo[n]
        
        # Main
        memo = {}
        return solve(n)