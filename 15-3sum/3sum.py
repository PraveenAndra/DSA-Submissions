class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i==0 or nums[i-1]!=nums[i]:
                self.twoSum(i,nums,res)
        return res
    
    def twoSum(self,i,nums,res):
        left = i+1
        right = len(nums)-1
        while left < right:
            sum = nums[left]+nums[right]+nums[i]
            if  sum== 0:
                res.append([nums[i],nums[left],nums[right]])
                left += 1
                right -=1 
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif sum < 0:
                left += 1
            else:
                right -=1
            
        