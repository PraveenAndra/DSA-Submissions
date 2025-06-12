class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []


        def backtrack(ind,arr):
            if ind > len(nums):
                return
            res.append(arr[:])
            for i in range(ind,len(nums)):
                if i!=ind and nums[i] == nums[i-1]:
                    continue
                arr.append(nums[i])
                backtrack(i+1,arr)
                arr.pop()
        nums.sort()
        backtrack(0,[])
        return res
