class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        def binary_search(left,right,mini):
            while left <= right:
                mid = left+(right-left)//2
                if nums[mid] < target:
                    left = mid+1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    if mini:
                        if mid == left or nums[mid-1] < target:
                            return mid
                        else:
                            right = mid-1
                    else:
                        if mid == right or nums[mid+1] > target:
                            return mid
                        else:
                            left = mid+1
            return -1
        return [binary_search(left,right,True),binary_search(left,right,False)] 
        
        