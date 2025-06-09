class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_s = nums[0]
        max_s = nums[0]
        res = max_s
        for i in range(1,len(nums)):
            num = nums[i]
            temp_max = max(num,max(min_s*num,max_s*num))
            min_s = min(num,min(min_s*num,max_s*num))
            max_s = temp_max
            res = max(res,max_s)
        return res



        