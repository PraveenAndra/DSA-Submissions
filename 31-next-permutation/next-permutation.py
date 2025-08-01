class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        ind = -1
        for i in range(l-1,0,-1):
            if nums[i] > nums[i-1]:
                ind = i-1
                break
        if ind==-1:
            for i in range(l//2):
                nums[i],nums[l-1-i] = nums[l-1-i],nums[i]
            return nums 
        else:
            for i in range(l-1,0,-1):
                if nums[i] > nums[ind]:
                    nums[i],nums[ind] = nums[ind],nums[i]
                    break
            nums[ind+1:] = nums[l-1:ind:-1]
            return nums
        
        