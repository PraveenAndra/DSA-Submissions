class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, -math.inf, -math.inf]
        for x in nums:
            m = x % 3
            new_dp = dp[:]
            for r in range(3):
                cand = dp[r] + x
                new_dp[(r + m) % 3] = max(new_dp[(r + m) % 3], cand)
            dp = new_dp
        return dp[0]
        # s = 0
        # buckets = [float('inf'),float('inf'),float('inf')]
        # for i in nums:
        #     rem = i%3
        #     buckets[rem] = min(buckets[rem],i)
        #     s += i
        # print(s,buckets)
        # if s%3 == 0:
        #     s = s 
        # elif s%3 == 1:
        #     s = s- buckets[1]
        # else:
        #     s = s - buckets[2]
        # return s if s != float('inf') else 0 


        