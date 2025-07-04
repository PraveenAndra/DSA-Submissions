class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        if len(nums) == 1:
            return nums[0]
        low = 0
        high = len(nums) - 1
        if nums[high] > nums[low]:
            return nums[0]
        while high >= low:
            mid = low + (high-low)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                low = mid+1 
            else: high = mid - 1
        # return nums[high]

        # left = 0
        # right = len(nums)-1
        # if len(nums)==1:
        #     return nums[0]
        # if nums[0] < nums[right]:
        #     return nums[0]
        # while right >= left:
        #     mid = left + (right-left)//2
        #     if nums[mid] > nums[mid+1]:
        #         return nums[mid+1]
        #     if nums[mid-1] > nums[mid]:
        #         return nums[mid]
        #     if nums[mid] > nums[0]:
        #         left = mid+1
        #     else:
        #         right = mid -1
                
        