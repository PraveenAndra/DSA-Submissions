class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # if len(nums) > 1 and len(set(nums)) == 1:
        #     return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]
        nums = [1]+nums+[1]
        @lru_cache(None)
        def backtrack(l,r):
            if r-l < 0:
                return 0
            m = 0
            for i in range(l,r+1):
                new_coins = nums[l-1]*nums[i]*nums[r+1]
                left = backtrack(l,i-1)
                right = backtrack(i+1,r)
                curr = new_coins+left+right
                m = max(m,curr)
            return m
        
        return backtrack(1,len(nums)-2)
        