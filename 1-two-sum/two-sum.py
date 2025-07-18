class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            curr = target - nums[i]
            if curr in lookup:
                return [lookup[curr],i]
            lookup[nums[i]] = i