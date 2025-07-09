class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        memo = [[float('-inf')]*(2*sum(nums)+1) for i in range(len(nums))]
        def countCombinations(nums,ind,currSum,target):
            nonlocal res
            if ind == len(nums):
                if currSum == target:
                    return 1
                else:
                    return 0
            # Add
            if memo[ind][currSum]== float('-inf'):
                add = countCombinations(nums,ind+1,currSum+nums[ind],target)
                # subract
                subtract = countCombinations(nums,ind+1,currSum - nums[ind], target)
                memo[ind][currSum] = add+ subtract
            return memo[ind][currSum]
        return countCombinations(nums,0,0,target)

        
        