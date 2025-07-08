class Solution:
    def jump(self, nums: List[int]) -> int:
        prev_max = 0
        prev_end =0
        count = 0
        for i in range(len(nums)-1):
            next = i+nums[i]
            prev_max = max(prev_max,next)
            if i==prev_end:
                prev_end = prev_max
                count += 1
                
        return count





        