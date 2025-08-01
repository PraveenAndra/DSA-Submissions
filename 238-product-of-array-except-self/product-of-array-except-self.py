class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1]*len(nums)
        right_prod = [1]*len(nums)
        
        for i in range(len(nums)-1):
            left_prod[i+1] = nums[i]*left_prod[i]
        for j in range(len(nums)-1,0,-1):
            right_prod[j-1] = nums[j] * right_prod[j]
        # print(left_prod,right_prod)
        res = []
        for i in range(len(nums)):
            res.append(left_prod[i]*(right_prod[i]))
        return res
        