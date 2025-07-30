class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(curr,counter):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for num in counter:
                if counter[num] > 0:
                    curr.append(num)
                    counter[num] -= 1
                    backtrack(curr,counter)
                    curr.pop()
                    counter[num] += 1
            

        backtrack([],Counter(nums))
        return res
        