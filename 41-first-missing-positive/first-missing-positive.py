class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            correct_idx = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        return n+1
