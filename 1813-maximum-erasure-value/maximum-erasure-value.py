class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if len(nums) == len(set(nums)):
            return sum(nums)
        lastInd = {}
        pref_sum = [0]*(len(nums)+1)
        maxScore = 0
        left = 0
        curr = 0
        for right in range(len(nums)):
            curr += nums[right]
            pref_sum[right+1] = curr
            if nums[right] in lastInd:
                left = lastInd[nums[right]]+1 if lastInd[nums[right]] >= left else left
            lastInd[nums[right]] = right
            maxScore = max(maxScore,curr - pref_sum[left])
        return maxScore

        