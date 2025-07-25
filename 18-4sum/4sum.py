class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def kSum(nums,target,k):
            res = []
            if not nums:
                return res
            avg = target // k
            if nums[0] > avg or nums[-1] < avg:
                return res
            if k == 2:
                return twoSum(nums,target)

            for i in range(len(nums)):
                if i==0 or nums[i-1]!=nums[i]:
                    for sub in kSum(nums[i+1:],target-nums[i],k-1):
                        res.append([nums[i]]+sub)
            return res
        
        def twoSum(nums,target):
            seen = set()
            res = []
            for num in nums:
                if len(res)==0 or res[-1][1]!=num:
                    if target - num in seen:
                        res.append([target - num,num])
                seen.add(num)
            return res
        nums.sort()
        return kSum(nums,target,4)
