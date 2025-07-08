class Solution:
    def canJump(self, nums: List[int]) -> bool:
        prev_max = 0
        for i in range(len(nums)):
            if i <= prev_max:
                prev_max = max(prev_max,i+nums[i])
        return prev_max >=len(nums)-1

        