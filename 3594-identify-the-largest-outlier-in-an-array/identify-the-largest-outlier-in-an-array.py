class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        s = sum(nums)
        lookup = defaultdict(int)
        for i in nums:
            lookup[i] += 1
        res = float('-inf')
        print(lookup)
        for i in nums:
            # consider i as outlier
            tot = s-i
            print(tot)
            if tot%2==0 and lookup[tot//2] > 0:
                if tot//2 == i and lookup[tot//2] == 1:
                    continue
                res = max(res,i)
        return res


        