class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        for num in nums:
            left,right = 0,len(sub)
            while left < right:
                mid = left + (right-left)//2
                if sub[mid] < num:
                    left = mid+1
                else:
                    right = mid
            if left >= len(sub):
                sub.append(num)
            else:
                sub[left] = num
        return len(sub)