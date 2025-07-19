class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        curr = 0
        for num in nums:
            if num >= curr+num:
                curr = num
            else:
                curr = curr+num
            maxSum = max(curr,maxSum)
        return maxSum
        