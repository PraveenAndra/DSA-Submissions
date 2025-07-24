class Solution:
    def rob(self, nums: List[int]) -> int:

        def robHouse(nums):
            one_back = 0
            two_back = 0
            res = 0
            for num in nums:
                res = max(two_back+num,one_back)
                two_back = one_back
                one_back = res
            return res
        if len(nums) == 1:
            return nums[0]
        return max(robHouse(nums[1::]),robHouse(nums[0:len(nums)-1]))
        
        