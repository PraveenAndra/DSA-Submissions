class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        sum = 0
        res = float('-inf')
        for i in range(len(nums)):
            sum = max(sum+nums[i],nums[i])
            res = max(res,sum)
        return res

        