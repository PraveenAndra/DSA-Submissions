class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        nums_set = set(nums)
        for num in nums_set:
            curr = 0
            if num-1 not in nums_set:
                curr += 1
                k = num
                while k+1 in nums_set:
                    curr += 1
                    k = k+1
                count = max(count,curr)
        return count
