class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        curr = 0
        for num in nums:
            if num >= curr+num  :
                curr = num
            else:
                curr = curr+num
            res = max(res,curr)
        return res
        