class Solution:
    def rob(self, nums: List[int]) -> int:
        one_back = 0
        two_back = 0
        for num in nums:
            res = max(num+two_back,one_back)
            two_back = one_back
            one_back = res
        return one_back