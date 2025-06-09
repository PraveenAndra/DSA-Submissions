class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2 !=0:
            return False
        @cache
        def dfs(nums,ind,summ):
            if summ == 0:
                return True
            if ind == 0 or summ < 0:
                return False
            res = (dfs(nums,ind-1,summ-nums[ind]) or dfs(nums,ind-1,summ))
            return res
        return dfs(tuple(nums),len(nums)-1,s//2)
        
        
        