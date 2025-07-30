class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findMaxSum(left,right,nums):
            if left> right:
                return float('-inf')
            
            leftSum = 0
            mid = (right +left)//2
            curr = 0
            for i in range(mid-1,left-1,-1):
                curr += nums[i]
                leftSum = max(leftSum,curr)
            right_sum = 0
            curr =0
            for i in range(mid+1,right+1):
                curr += nums[i]
                right_sum = max(right_sum,curr)
            
            return max(leftSum+right_sum+nums[mid],findMaxSum(left,mid-1,nums),findMaxSum(mid+1,right,nums))
        return findMaxSum(0,len(nums)-1,nums)
            