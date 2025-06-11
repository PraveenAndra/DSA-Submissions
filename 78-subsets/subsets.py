class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def findSubs(ind,arr):
            res.append(arr[:])
            if ind > len(nums) - 1:
                return arr
            for i in range(ind,len(nums)):
                arr.append(nums[i])
                findSubs(i+1,arr)
                arr.pop()
        findSubs(0,[])
        return res

        