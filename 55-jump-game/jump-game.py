class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)):
            if i <=maxReach:
                maxReach = max(maxReach,i+nums[i])
        return maxReach >= (len(nums) -1)
        
        