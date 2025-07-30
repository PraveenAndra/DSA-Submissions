class Solution:
    def jump(self, nums: List[int]) -> int:
        prev_end = 0
        max_reach = 0
        res = 0
        for i in range(len(nums)-1):
            max_reach = max(max_reach,i+nums[i])
            if i == prev_end:
                res += 1
                prev_end = max_reach
        return res

        