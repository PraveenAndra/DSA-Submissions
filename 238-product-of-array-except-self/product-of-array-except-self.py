class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [1]
        left = [1]
        for i in nums:
            left.append(i*left[-1])
        for i in nums[::-1]:
            right.append(i*right[-1])
        
        right = right[::-1]
        # print(left,right)
        res = []
        for i in range(len(nums)):
            res.append(left[i]*right[i+1])
        return res