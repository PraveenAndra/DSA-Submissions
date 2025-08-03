class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1]*len(nums)
        n = len(nums)
        for i in range(2*n):
            ind = i%n
            while stack and nums[stack[-1]] < nums[ind]:
                prev = stack.pop()
                res[prev] = nums[ind]
            if i<n:
                stack.append(ind)
        return res


        