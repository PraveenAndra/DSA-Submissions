class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1

        while low <= high:
            pivot = low + (high - low)//2
            if nums[pivot] == target:
                return True
            if nums[pivot] == nums[low]:
                low += 1
                continue
            pivotFirst = (nums[low] <= nums[pivot])
            targetFirst = (nums[low] <= target)
            if pivotFirst ^ targetFirst:
                if pivotFirst:
                    low = pivot+1
                else:
                    high = pivot - 1
            else:
                if nums[pivot] < target:
                    low = pivot + 1
                else:
                    high = pivot - 1
        return False