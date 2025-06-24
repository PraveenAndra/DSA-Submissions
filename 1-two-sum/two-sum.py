class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            req = target - nums[i]
            if req in lookup:
                return [lookup[req],i]
            lookup[nums[i]] = i
        return 


            
            