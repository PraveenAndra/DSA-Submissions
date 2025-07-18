class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[1]*k for i in range(n)]
        @cache
        def dfs(ind):
            if ind == n-1:
                return
            for i in range(ind+1,n):
                nr = (nums[ind]+nums[i]) % k
                if dp[i][nr] == 1:
                    dfs(ind+1)
                dp[ind][nr] = max(dp[ind][nr],dp[i][nr]+1)
        dfs(0)
        return max([max(i) for i in dp])
            

