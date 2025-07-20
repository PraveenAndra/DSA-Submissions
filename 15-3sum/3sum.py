class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i==0 or nums[i] != nums[i-1]:
                res.extend(self.twoSum(nums[i+1:],nums[i]))
        return res

    def twoSum(self,nums,num):
        left = 0
        right = len(nums)-1
        res = set()
        while left < right:
            s = nums[left]+nums[right]+num
            if s == 0:
                res.add((num,nums[left],nums[right]))
                left+=1
                right -=1
            elif s < 0:
                left += 1
            else:
                right -= 1
        return res