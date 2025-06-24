class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curr = maxSub
        for i in nums[1:]:
            if i > curr+i:
                curr = i
            else:
                curr = curr+i
            maxSub = max(curr,maxSub)
        return maxSub

