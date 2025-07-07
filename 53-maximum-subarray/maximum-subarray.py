class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        curr = 0
        for i in range(len(nums)):
            if nums[i] >= nums[i] + curr:
                curr = nums[i]
            else:
                curr += nums[i]
            maxSum = max(curr,maxSum)
        return maxSum
        