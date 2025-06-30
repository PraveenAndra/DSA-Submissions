class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # left = 0
        maxSum = nums[0]
        curr = nums[0]
        for right in range(1,len(nums)):
            if nums[right] >= curr+nums[right]:
                # left = right
                curr = nums[right]
            else:
                curr += nums[right]
            maxSum = max(curr,maxSum)
        return maxSum
        