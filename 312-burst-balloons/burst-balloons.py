class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # if len(nums) > 1 and len(set(nums)) == 1:
        #     return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]
        # nums = [1]+nums+[1]
        # @lru_cache(None)
        # def backtrack(l,r):
        #     print(l,r)
        #     if r-l < 0:
        #         return 0
        #     m = 0
        #     for i in range(l,r+1):
        #         new_coins = nums[l-1]*nums[i]*nums[r+1]
        #         left = backtrack(l,i-1)
        #         right = backtrack(i+1,r)
        #         curr = new_coins+left+right
        #         m = max(m,curr)
            
        #     return m
        
        # return backtrack(1,len(nums)-2)

        # special case
        # if len(nums) > 1 and len(set(nums)) == 1:
        #     return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        # # handle edge case
        # nums = [1] + nums + [1]
        # n = len(nums)
        # # dp[i][j] represents
        # # maximum if we burst all nums[left]...nums[right], inclusive
        # dp = [[0] * n for _ in range(n)]

        # # do not include the first one and the last one
        # # since they are both fake balloons added by ourselves and we can not
        # # burst them
        # for left in range(n - 2, 0, -1):
        #     for right in range(left, n - 1):
        #         # find the last burst one in nums[left]...nums[right]
        #         for i in range(left, right + 1):
        #             # nums[i] is the last burst one
        #             gain = nums[left - 1] * nums[i] * nums[right + 1]
        #             # recursively call left side and right side
        #             remaining = dp[left][i - 1] + dp[i + 1][right]
        #             # update
        #             dp[left][right] = max(remaining + gain, dp[left][right])
        #             print(i,left,right,gain,remaining)
        #             print(dp)
        # return dp[1][n - 2]


        # 
        nums = [1]+nums+[1]
        n = len(nums)
        dp = [[0]*n for i in range(n)]

        for length in range(n-2):
            for start in range(1,n-length-1):
                end = start + length
                for burst in range(start,end+1):
                    coins = nums[start-1]*nums[burst]*nums[end+1]
                    additional = dp[start][burst-1]+dp[burst+1][end]
                    dp[start][end] = max(coins+additional,dp[start][end])
        # print(dp)
        return dp[1][n-2]

        