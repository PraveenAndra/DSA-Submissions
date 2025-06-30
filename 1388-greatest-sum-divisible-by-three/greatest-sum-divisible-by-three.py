class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, -math.inf, -math.inf]
        for x in nums:
            m = x % 3
            new_dp = dp[:]  # copy current bests
            for r in range(3):
                # try adding x to a sum that was ≡ r
                cand = dp[r] + x
                new_dp[(r + m) % 3] = max(new_dp[(r + m) % 3], cand)
            dp = new_dp
        return dp[0]


        